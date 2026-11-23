"""Traceroute support is represented by persisted hop records; UI integration is pending."""
class TracerouteService:
    def parse(self, trace): return [{"hop_number":i+1,"address":hop.get("ipaddr"),"latency":hop.get("rtt")} for i,hop in enumerate(trace or [])]
