from app.visualization.graph_builder import build_graph
from app.visualization.network_graph import render_graph

class GraphService:
    def render(self, hosts): 
        return render_graph(build_graph(hosts))
