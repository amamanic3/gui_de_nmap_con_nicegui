from nicegui import ui
from app.services.scan_service import ScanService

def render():
    ui.label("Network discovery").classes("text-2xl font-bold")
    ui.label("Ping discovery can miss hosts that block probes; an unresponsive host is not necessarily offline.")
    target=ui.input("Authorized IPv4/IPv6 target or subnet",placeholder="192.168.1.0/24").classes("w-full")
    consent=ui.checkbox("I am authorized to discover this network")
    async def discover():
        try: 
            await ScanService().start({"target":target.value,"profile":"ping","authorized":consent.value})
            ui.notify("Discovery submitted",type="positive")
        except Exception as exc: 
            ui.notify(str(exc),type="negative")
    ui.button("Discover devices",on_click=discover)
