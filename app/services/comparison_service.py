from sqlalchemy import select
from app.database.connection import SessionLocal
from app.database.models import Scan, HostObservation, Port, Host

class ComparisonService:
    def compare(self, first: int, second: int):
        with SessionLocal() as s:
            a=s.get(Scan,first); b=s.get(Scan,second)
            if not a or not b: raise ValueError("Both scans must exist.")
            def snapshot(scan):
                result={}
                for o in s.scalars(select(HostObservation).where(HostObservation.scan_id==scan.id)):
                    result[o.host.ip_address]={(p.protocol,p.port_number,p.state) for p in o.ports}
                return result
            x,y=snapshot(a),snapshot(b); return {"new_hosts":sorted(set(y)-set(x)),"missing_hosts":sorted(set(x)-set(y)),"port_changes":{ip:{"opened":sorted(y[ip]-x[ip]),"closed":sorted(x[ip]-y[ip])} for ip in set(x)&set(y) if x[ip]!=y[ip]}}
