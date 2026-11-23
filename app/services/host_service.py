from app.database.connection import SessionLocal
from app.database.repositories import InventoryRepository

class HostService:
    def list_hosts(self):
        with SessionLocal() as s: return InventoryRepository(s).hosts()
    def counts(self):
        with SessionLocal() as s: return InventoryRepository(s).counts()
