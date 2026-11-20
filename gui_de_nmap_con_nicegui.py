#!/usr/bin/env python3
from nicegui import events, ui
import nmap


def add_row(nm, h) -> None:
    new_id = max((dx['id'] for dx in table.rows), default=-1) + 1
    table.rows.append({'id': new_id, 'host': h, 'hostname': nm[h].hostname(), 'state': nm[h].state()})
    #ui.notify(f'Added new row with ID {new_id}')
    table.update()

def clean() -> None:
    table.rows[:] = []
    #ui.notify(f'Deleted row with ID {e.args["id"]}')
    table.update()

hosts = ''
arguments = ''

def port_scan() -> None:
    global hosts
    global arguments
    hosts = network.value
    arguments = '' 
    search_bar.text = '> nmap '+arguments+' '+hosts 

def ping_scan() -> None:
    global hosts
    global arguments
    hosts = network.value
    arguments = '-sn' 
    search_bar.text = '> nmap '+arguments+' '+hosts 

def scan() -> None:
    clean()
    nm = nmap.PortScanner()
    nm.scan(hosts=hosts, arguments=arguments)
    for h in nm.all_hosts():
        add_row(nm, h)
    
    
search_bar = ui.label('')
network = ui.input(label='Network', placeholder='e.g. 192.168.3-5,7.1')
ui.button('port scan', color='green', on_click=port_scan).classes('w-50')
ui.button('ping scan', color='green', on_click=ping_scan).classes('w-50')
ui.button('Scan', icon='search', color='accent', on_click=scan).classes('w-100')
table = ui.table(columns=[
    {'name': 'host', 'label': 'Host', 'field': 'host', 'align': 'left'},
    {'name': 'hostname', 'label': 'Hostname', 'field': 'hostname', 'align': 'left'},
    {'name': 'state', 'label': 'State', 'field': 'state', 'align': 'left'},
], rows=[], row_key='name').classes('w-100')


ui.run()
