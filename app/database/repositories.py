from sqlalchemy import select, func
from sqlalchemy.orm import Session
from app.database.models import Scan, Host, HostObservation, Port

class ScanRepository:
    def __init__(self, session: Session): self.session = session
    def recent(self, limit: int = 50): return list(self.session.scalars(select(Scan).order_by(Scan.started_at.desc()).limit(limit)))
    def get(self, scan_id: int): return self.session.get(Scan, scan_id)

class InventoryRepository:
    def __init__(self, session: Session): self.session = session
    def counts(self) -> dict[str, int]:
        return {"hosts": self.session.scalar(select(func.count(Host.id))) or 0, "ports": self.session.scalar(select(func.count(Port.id))) or 0}
    def hosts(self): return list(self.session.scalars(select(Host).order_by(Host.ip_address)))
