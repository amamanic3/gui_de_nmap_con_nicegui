from nicegui import ui
from app.services.host_service import HostService
from app.database.connection import SessionLocal
from app.database.repositories import ScanRepository

def render():
    counts=HostService().counts()
    ui.label("Network inventory overview").classes("text-2xl font-bold")
    with ui.row().classes("w-full"):
        with ui.card(): ui.label("Known hosts"); ui.label(str(counts["hosts"])).classes("text-3xl font-bold")
        with ui.card(): ui.label("Recorded ports"); ui.label(str(counts["ports"])).classes("text-3xl font-bold")
    with SessionLocal() as s: scans=ScanRepository(s).recent(8)
    ui.label("Recent scans").classes("text-xl mt-6")
    ui.table(columns=[{"name":"target","label":"Target","field":"target"},{"name":"profile","label":"Profile","field":"profile"},{"name":"status","label":"Status","field":"status"}],rows=[{"target":x.target_scope,"profile":x.scan_profile,"status":x.status} for x in scans]).classes("w-full")
