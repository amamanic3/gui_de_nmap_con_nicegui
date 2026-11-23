import os
import platform

def permission_report() -> dict[str, str | bool]:
    elevated = (os.name == "nt" and _windows_admin()) or (os.name != "nt" and hasattr(os, "geteuid") and os.geteuid() == 0)
    return {"elevated": elevated, "summary": "Elevated privileges detected." if elevated else "Standard user. SYN, UDP, and OS detection may require administrator/root privileges or Linux capabilities."}

def _windows_admin() -> bool:
    try:
        import ctypes
        return bool(ctypes.windll.shell32.IsUserAnAdmin())
    except (AttributeError, OSError):
        return False
