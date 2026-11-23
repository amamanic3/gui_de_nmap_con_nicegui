from app.services.whitelist_service import WhitelistService

def test_whitelist_requires_identifier():
    try: WhitelistService().add()
    except ValueError as exc: assert "identifier" in str(exc)
    else: raise AssertionError("identifier should be required")
