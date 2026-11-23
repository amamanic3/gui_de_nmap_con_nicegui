from nicegui import ui
from app.services.scan_service import ScanService
from app.scanner.scan_profiles import PROFILES

def render():
    ui.label("Authorized scan").classes("text-2xl font-bold")
    ui.label("Only scan systems and ranges you are authorized to assess.").classes("text-amber-300")
    target=ui.input("Target (IP, hostname, or CIDR)",placeholder="192.168.1.0/24").classes("w-full")
    profile=ui.select({k:v["description"] for k,v in PROFILES.items()},value="ping",label="Scan profile").classes("w-full")
    ports=ui.input("Ports (optional)",placeholder="22,80,443 or 1-1024").classes("w-full")
    authorized=ui.checkbox("I am authorized to scan this target")
    status=ui.label()
    async def start():
        try:
            result=await ScanService().start({"target":target.value,"profile":profile.value,"ports":ports.value or None,"authorized":authorized.value})
            status.text=f"Scan {result['id']} submitted · {result['status']}"
            ui.notify("Scan submitted",type="positive")
        except Exception as exc: 
            status.text=str(exc)
            ui.notify(str(exc),type="negative")
    ui.button("Start scan",on_click=start,color="primary")
