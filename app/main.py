from nicegui import ui
from app.config import settings
from app.database.connection import initialize_database
from app.utils.logger import configure_logging
from app.ui.layout import shell

def setup():
    configure_logging(); initialize_database()
    from app.ui import dashboard, scan_page, discovery_page, hosts_page, ports_page, whitelist_page, topology_page, history_page, reports_page, settings_page
    pages={"/":("Dashboard",dashboard.render),"/scanner":("Scanner",scan_page.render),"/discovery":("Network discovery",discovery_page.render),"/hosts":("Hosts",hosts_page.render),"/ports":("Ports and services",ports_page.render),"/whitelist":("Whitelist",whitelist_page.render),"/topology":("Network topology",topology_page.render),"/history":("Scan history",history_page.render),"/reports":("Reports",reports_page.render),"/settings":("Settings",settings_page.render)}
    for path,(title,render) in pages.items():
        def page(title=title,render=render):
            shell(title)
            with ui.column().classes("w-full max-w-7xl mx-auto p-6 gap-4"): render()
        ui.page(path)(page)

if __name__ in {"__main__", "__mp_main__","app.main"}:
    setup(); ui.run(host=settings.bind_host,port=settings.bind_port,title="Nmap Network Discovery",dark=True,show=False)
