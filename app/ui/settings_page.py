from nicegui import ui
from app.config import settings
from app.platform.os_detector import get_platform_info
from app.platform.nmap_detector import detect_nmap
from app.platform.permissions import permission_report
from app.platform.interfaces import list_interfaces

def render():
    ui.label("Compatibility and settings").classes("text-2xl font-bold")
    info=get_platform_info(); nmap=detect_nmap(settings.nmap_path); perms=permission_report()
    ui.label(f"Platform: {info['system']} {info['release']} ({info['machine']})")
    ui.label(f"Nmap: {'available' if nmap['available'] else 'not available'} · {nmap['version'] or nmap['error']}")
    ui.label(f"Executable: {nmap['path'] or 'not found'}")
    ui.label(str(perms["summary"]))
    ui.label("Interfaces").classes("text-lg mt-4")
    ui.table(columns=[{"name":"name","label":"Interface","field":"name"},{"name":"addresses","label":"Addresses","field":"addresses"}],rows=list_interfaces())
    ui.label(f"Database: {settings.database_url}")
    if not nmap["available"]: ui.markdown("Install Nmap from [nmap.org](https://nmap.org/download.html) (Windows), or your distribution package manager (`sudo apt install nmap` on Ubuntu/Debian).")
