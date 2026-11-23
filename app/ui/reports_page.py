from nicegui import ui
from app.services.host_service import HostService
from app.services.report_service import ReportService

def render():
    ui.label("Reports and exports").classes("text-2xl font-bold")
    kind=ui.select(["csv","json"],value="csv",label="Format"); name=ui.input("Filename",value="host-inventory.csv")
    status=ui.label()
    def export():
        try:
            rows=[{"ip_address":h.ip_address,"hostname":h.hostname,"mac_address":h.mac_address,"status":h.status,"operating_system":h.operating_system,"first_seen":h.first_seen,"last_seen":h.last_seen} for h in HostService().list_hosts()]
            path=ReportService().export(kind.value,rows,name.value); status.text=f"Saved: {path}"
        except Exception as exc: status.text=str(exc)
    ui.button("Export host inventory",on_click=export)
    ui.label("Files are written to the local reports folder. PDF and Nmap XML exporters are available to application code but not wired to this screen yet.")
