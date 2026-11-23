from nicegui import ui
from app.services.host_service import HostService
from app.services.graph_service import GraphService

def render():
    ui.label("Network topology").classes("text-2xl font-bold")
    html=GraphService().render(HostService().list_hosts())
    #ui.html(html,sanitize=False).classes("w-full")
    ui.add_body_html(html)
    ui.label("Only hosts are shown. Links are omitted unless observed; IP proximity is not treated as a relationship.").classes("text-sm text-slate-400")
