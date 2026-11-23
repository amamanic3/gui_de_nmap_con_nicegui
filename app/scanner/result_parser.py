from dataclasses import dataclass, field
from typing import Any

@dataclass
class ParsedPort:
    number: int
    protocol: str
    state: str
    service: dict[str, Any] = field(default_factory=dict)

@dataclass
class ParsedHost:
    address: str
    hostname: str | None
    state: str
    mac: str | None
    os: str | None
    ports: list[ParsedPort]

def parse_scan(scanner) -> list[ParsedHost]:
    hosts = []
    for address in scanner.all_hosts():
        item = scanner[address]
        names = item.hostname() if callable(item.hostname) else item.hostname
        hostname = names or None
        ports = []
        for proto in item.all_protocols():
            for number, info in item[proto].items():
                ports.append(ParsedPort(int(number), proto, info.get("state", "unknown"), info.get("product") and {k: info.get(k) for k in ("name", "product", "version", "extrainfo")} or {"name": info.get("name")}))
        os_info = None
        matches = item.get("osmatch", [])
        if matches: os_info = matches[0].get("name")
        hosts.append(ParsedHost(address, hostname, item.state(), item.get("addresses", {}).get("mac"), os_info, ports))
    return hosts
