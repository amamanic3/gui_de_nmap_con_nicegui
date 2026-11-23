from app.utils.validators import ScanRequest
from app.scanner.scan_profiles import PROFILES

def validate_scan(data: dict) -> ScanRequest:
    request = ScanRequest(**data)
    if request.profile not in PROFILES and request.profile != "custom":
        raise ValueError("Select a supported scan profile.")
    if not request.authorized:
        raise ValueError("Confirm that you are authorized to scan this target.")
    return request
