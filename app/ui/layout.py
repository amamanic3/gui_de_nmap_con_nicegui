from nicegui import ui

def shell(active: str):
    ui.dark_mode().enable()
    with ui.left_drawer(value=True).classes("bg-slate-950 text-slate-100"):
        ui.label("NMAP / DISCOVERY").classes("text-lg font-bold p-4")
        for label,path in [("Dashboard","/"),("Scanner","/scanner"),("Discovery","/discovery"),("Hosts","/hosts"),("Ports and services","/ports"),("Whitelist","/whitelist"),("Topology","/topology"),("History","/history"),("Reports","/reports"),("Settings","/settings")]:
            ui.link(label,path).classes("block px-4 py-2 rounded hover:bg-slate-800")
    with ui.header().classes("bg-slate-900 items-center justify-between"):
        ui.label(active).classes("text-xl font-semibold"); ui.label("Authorized network operations only").classes("text-xs text-amber-300")
