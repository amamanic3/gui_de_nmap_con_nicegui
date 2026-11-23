from app.database.connection import SessionLocal
from app.database.models import WhitelistDevice, Host

class WhitelistService:
    def add(self, **data):
        if not any(data.get(k) for k in ("ip_address", "mac_address", "hostname")): raise ValueError("At least one device identifier is required.")
        with SessionLocal() as s:
            row=WhitelistDevice(**data); s.add(row); s.commit(); s.refresh(row); return row.id
    def list(self):
        with SessionLocal() as s: return [{"id":d.id,"ip_address":d.ip_address,"mac_address":d.mac_address,"hostname":d.hostname,"description":d.description,"owner":d.owner,"authorization_status":d.authorization_status} for d in s.query(WhitelistDevice).all()]
    def compare(self):
        with SessionLocal() as s:
            approved=s.query(WhitelistDevice).all(); output=[]
            for h in s.query(Host).all():
                matched=any((d.ip_address and d.ip_address==h.ip_address) or (d.mac_address and d.mac_address.lower()==(h.mac_address or "").lower()) or (d.hostname and d.hostname.lower()==(h.hostname or "").lower()) for d in approved)
                output.append({"ip_address":h.ip_address,"hostname":h.hostname,"authorization_status":"authorized" if matched else "unclassified"})
            return output
