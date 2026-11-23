from app.visualization.graph_builder import build_graph

def test_graph_does_not_invent_edges():
    graph=build_graph([{"ip_address":"192.0.2.1","status":"up"}])
    assert len(graph["nodes"])==1 and graph["edges"]==[]
