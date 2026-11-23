from xml.etree.ElementTree import Element, SubElement, ElementTree
from pathlib import Path

def export_xml(data: dict, path: Path) -> None:
    root=Element("nmaprun", attrib={"scanner":"nmap-gui","version":"normalized"})
    for host in data.get("hosts",[]):
        h=SubElement(root,"host"); SubElement(h,"address",addr=str(host.get("ip_address","")),addrtype="ipv4")
        for port in host.get("ports",[]):
            p=SubElement(SubElement(h,"ports"),"port",protocol=str(port.get("protocol","tcp")),portid=str(port.get("port_number","")))
            SubElement(p,"state",state=str(port.get("state","unknown")))
    ElementTree(root).write(path,encoding="utf-8",xml_declaration=True)
