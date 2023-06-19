#Asaf Ben Or
#Alon Artimonov
import networkx as nx
from networkx.algorithms import isomorphism
from collections import defaultdict
from itertools import combinations
import copy

def generate_motifs(n, edges):
    G = nx.DiGraph()
    G.add_edges_from(edges)
    subgraphs = [G.subgraph(nodes).copy() for nodes in combinations(G.nodes, n)]
    motif_instances = find_motif_instances(subgraphs, n)
    filename = f"motifs.txt"
    with open(filename, "w") as file:
     file.write(f"n={n}\n")
     motif_id = 1
     for motif, instances in motif_instances.items():
         file.write(f"#{motif_id}\n")
         file.write(f"count={len(instances)}\n")
         for instance in instances:
             for edge in instance.edges:
                 file.write(f"{edge[1]} {edge[0]}\n")
         motif_id += 1
         file.write("")

def relabel_graph(G):
    """Relabels the nodes of a graph in ascending order."""
    mapping = {old_label: new_label for new_label, old_label in enumerate(sorted(G.nodes))}
    return nx.relabel_nodes(G, mapping)

def find_motif_instances(subgraphs, n):
    motif_instances = defaultdict(list)
    for subgraph in subgraphs:
        if subgraph.number_of_edges() == 0 or subgraph.number_of_edges() < n-1 or subgraph.number_of_nodes() != n:
            continue
        sorted_nodes = sorted(subgraph.nodes)
        sorted_subgraph = nx.DiGraph(nx.adjacency_matrix(subgraph, nodelist=sorted_nodes))
        added = False
        for motif in motif_instances.copy():
            if nx.adjacency_matrix(sorted_subgraph).todense().tolist() == nx.adjacency_matrix(motif).todense().tolist():
                motif_instances[motif].append(subgraph)
                added = True
                break
        if not added:
            motif_instances[copy.deepcopy(sorted_subgraph)].append(subgraph)
    return motif_instances


edges = [(1,2),(1,4),(2,3)]
n=4
generate_motifs(n, edges)
