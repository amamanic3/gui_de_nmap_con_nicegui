import nmap
from app.config import settings
from app.scanner.scan_profiles import PROFILES
from app.scanner.scan_validator import validate_scan
from app.scanner.result_parser import parse_scan

class NmapEngine:
    def scan(self, data: dict):
        request = validate_scan(data)
        scanner = nmap.PortScanner(nmap_search_path=(settings.nmap_path,) if settings.nmap_path else ())
        args = PROFILES[request.profile]["arguments"] if request.profile in PROFILES else "-sT"
        if request.ports: args += f" -p {request.ports}"
        scanner.scan(hosts=request.target, arguments=args, timeout=settings.scan_timeout_seconds)
        return parse_scan(scanner)
