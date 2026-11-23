from app.scanner.scan_validator import validate_scan

def test_ping_target_validation():
    assert validate_scan({"target":"192.0.2.1","profile":"ping","authorized":False}).target=="192.0.2.1"

def test_port_scan_requires_authorization():
    try: validate_scan({"target":"192.0.2.1","profile":"common_tcp","authorized":False})
    except ValueError as exc: assert "authorized" in str(exc)
    else: raise AssertionError("authorization should be required")
