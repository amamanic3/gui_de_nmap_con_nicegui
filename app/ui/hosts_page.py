from nicegui import ui
from app.services.host_service import HostService

def render():
    ui.label("Hosts").classes("text-2xl font-bold")
    rows=[{"ip":h.ip_address,"hostname":h.hostname or "—","mac":h.mac_address or "—","state":h.status,"os":h.operating_system or "—","last_seen":str(h.last_seen)} for h in HostService().list_hosts()]
    ui.table(columns=[{"name":k,"label":label,"field":k,"sortable":True} for k,label in [("ip","IP address"),("hostname","Hostname"),("mac","MAC"),("state","Status"),("os","Operating system"),("last_seen","Last seen")]],rows=rows, row_key="ip").classes("w-full")
