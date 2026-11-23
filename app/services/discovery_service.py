from app.services.scan_service import ScanService

class DiscoveryService:
    def __init__(self, scans=None): self.scans = scans or ScanService()
    async def discover(self, target, authorized): return await self.scans.start({"target": target, "profile": "ping", "authorized": authorized})
