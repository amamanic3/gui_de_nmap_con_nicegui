from pyvis.network import Network

def render_graph(graph) -> str:
    net=Network(height="650px",width="100%",directed=False,cdn_resources="in_line",bgcolor="#111827",font_color="#e5e7eb")
    for n in graph["nodes"]: 
        net.add_node(n["id"],label=n["label"],title=n["title"],color=n["color"])
    for e in graph["edges"]: 
        net.add_edge(e["from"],e["to"],title=e.get("evidence","observed"))
    return net.generate_html()
