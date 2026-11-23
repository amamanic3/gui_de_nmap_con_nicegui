from nicegui import ui
from app.services.whitelist_service import WhitelistService

def render():
    ui.label("Authorized devices").classes("text-2xl font-bold")
    ip=ui.input("IP address"); mac=ui.input("MAC address"); host=ui.input("Hostname"); desc=ui.input("Description"); owner=ui.input("Owner / department")
    table=ui.table(columns=[{"name":k,"label":k.replace("_"," ").title(),"field":k} for k in ["ip_address","mac_address","hostname","description","owner","authorization_status"]],rows=WhitelistService().list()).classes("w-full")
    def add():
        try: WhitelistService().add(ip_address=ip.value or None,mac_address=mac.value or None,hostname=host.value or None,description=desc.value,owner=owner.value); table.rows=WhitelistService().list(); table.update(); ui.notify("Device registered",type="positive")
        except Exception as exc: ui.notify(str(exc),type="negative")
    ui.button("Register device",on_click=add); ui.button("Compare inventory",on_click=lambda: ui.notify(str(WhitelistService().compare()),timeout=7000))
