from app.discovery.network_discovery import validate_network

def test_ipv6_target(): assert validate_network("2001:db8::/64")=="2001:db8::/64"
