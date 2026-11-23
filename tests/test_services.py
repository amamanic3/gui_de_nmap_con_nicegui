from app.scanner.result_parser import parse_scan

class FakeHost(dict):
    def state(self): return "up"
    def hostname(self): return ""
    def all_protocols(self): return []

class FakeScanner:
    def all_hosts(self): return ["192.0.2.1"]
    def __getitem__(self,key): return FakeHost(addresses={"ipv4":key},osmatch=[])

def test_parser_accepts_host_without_ports():
    result=parse_scan(FakeScanner())
    assert result[0].address=="192.0.2.1" and result[0].ports==[]
