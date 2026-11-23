def add_to_network(ip):
    #net.add_edge("192.168.0.0",ip,title="belongs to")
    pass

def build_graph(hosts):
    nodes=[]
    edges=[]
    nodes.append({"id":"192.168.0.0","label":"192.168.0.0","title":"network","color":"gray"})
    for host in hosts:
        ip=getattr(host,"ip_address",host.get("ip_address") if isinstance(host,dict) else "unknown")
        status=getattr(host,"status",host.get("status","unknown") if isinstance(host,dict) else "unknown")
        nodes.append({"id":ip,"label":ip,"title":f"{ip} — {status}","color":"#22c55e" if status=="up" else "#64748b"})
        # edges.append(add_to_network(ip))
        edges.append({"from":"192.168.0.0", "to":ip})
    return {"nodes":nodes,"edges":edges}
