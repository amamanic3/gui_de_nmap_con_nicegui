PROFILES = {
    "ping": {"arguments": "-sn", "description": "Host discovery only; no port scan."},
    "common_tcp": {"arguments": "-sT -F", "description": "TCP connect scan of common ports."},
    "service_tcp": {"arguments": "-sT -sV -F", "description": "Common TCP ports with service/version detection."},
    "udp_common": {"arguments": "-sU --top-ports 20", "description": "Top 20 UDP ports; elevated privileges usually required."},
}
