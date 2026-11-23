from nicegui import ui
from app.database.connection import SessionLocal
from app.database.repositories import ScanRepository

def render():
    ui.label("Scan history").classes("text-2xl font-bold")
    with SessionLocal() as s: rows=[{"id":x.id,"target":x.target_scope,"profile":x.scan_profile,"status":x.status,"started":str(x.started_at),"duration":x.duration or "—"} for x in ScanRepository(s).recent(200)]
    ui.table(columns=[{"name":k,"label":v,"field":k,"sortable":True} for k,v in [("id","ID"),("target","Target"),("profile","Profile"),("status","Status"),("started","Started"),("duration","Duration")]],rows=rows).classes("w-full")
