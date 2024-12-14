import networkx as nx

def build_graph(edges):
    G = nx.Graph()
    G.add_edges_from(edges)
    return G

def get_clusters(edges):
    G = build_graph(edges)
    clusters = list(nx.connected_components(G))
    return [list(cluster) for cluster in clusters]
