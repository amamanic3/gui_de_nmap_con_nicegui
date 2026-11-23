import json, time
from datetime import datetime, timezone
from app.database.connection import SessionLocal
from app.database.models import Scan, Host, HostObservation, Port, Service
from app.scanner.scan_manager import ScanManager

class ScanService:
    def __init__(self, manager=None): self.manager = manager or ScanManager()
    async def start(self, request):
        session = SessionLocal()
        row = Scan(target_scope=request["target"], scan_profile=request["profile"], scan_configuration=json.dumps({k:v for k,v in request.items() if k != "authorized"}), status="running")
        session.add(row); session.commit(); session.refresh(row); scan_id = row.id; session.close()
        job = await self.manager.submit(request)
        asyncio_task = __import__("asyncio").create_task(self._persist_when_done(scan_id, job))
        return {"id": scan_id, "job_id": job.id, "status": job.status}
    async def _persist_when_done(self, scan_id, job):
        import asyncio
        while job.status in {"queued", "running"}: await asyncio.sleep(.5)
        with SessionLocal() as s:
            scan = s.get(Scan, scan_id); scan.status = job.status; scan.completed_at = datetime.now(timezone.utc)
            if job.error: scan.error_message = job.error
            for item in job.result:
                host = s.query(Host).filter_by(ip_address=item.address).one_or_none()
                if host is None: host = Host(ip_address=item.address); s.add(host); s.flush()
                host.hostname = item.hostname or host.hostname; host.mac_address = item.mac or host.mac_address; host.status = item.state; host.operating_system = item.os or host.operating_system; host.last_seen = datetime.now(timezone.utc)
                obs = HostObservation(host=host, scan=scan); s.add(obs); s.flush()
                for p in item.ports:
                    port = Port(observation=obs, port_number=p.number, protocol=p.protocol, state=p.state); s.add(port)
                    d=p.service or {}; s.add(Service(port=port, service_name=d.get("name"), product=d.get("product"), version=d.get("version"), extra_information=d.get("extrainfo")))
            s.commit()
