import socket

def list_interfaces() -> list[dict[str, str]]:
    try:
        import psutil
        return [{"name": name, "addresses": ", ".join(a.address for a in addrs if a.family in (socket.AF_INET, socket.AF_INET6))} for name, addrs in psutil.net_if_addrs().items()]
    except ImportError:
        return [{"name": name, "addresses": ""} for _, name in socket.if_nameindex()]
