from app.utils.validators import ScanRequest

def validate_network(target: str) -> str:
    request=ScanRequest(target=target)
    return request.target
