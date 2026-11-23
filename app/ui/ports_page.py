from nicegui import ui
from app.database.connection import SessionLocal
from app.database.models import Port

def render():
    ui.label("Ports and services").classes("text-2xl font-bold")
    with SessionLocal() as s:
        rows=[{"host":p.observation.host.ip_address,"port":p.port_number,"protocol":p.protocol,"state":p.state,"service":p.service.service_name if p.service else "—","product":p.service.product if p.service else "—","version":p.service.version if p.service else "—"} for p in s.query(Port).all()]
    cols=[{"name":k,"label":v,"field":k,"sortable":True} for k,v in [("host","Host"),("port","Port"),("protocol","Protocol"),("state","State"),("service","Service"),("product","Product"),("version","Version")]]
    ui.table(columns=cols,rows=rows).classes("w-full")
