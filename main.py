import itertools
import networkx as nx

def generate_subgraphs(n):
    edges = list(itertools.permutations(range(1, n+1), 2))#starting by getting a list of all permutations
    subgraphs = []
    for r in range(1, len(edges)+1):#exclude empty subsets
        for subset in itertools.combinations(edges, r):
            graph = nx.DiGraph(list(subset))
            if len(graph.nodes) == n and nx.number_weakly_connected_components(graph) == 1:#making sure it has all nodes and that is connected
                if not any(nx.is_isomorphic(graph, sg) for sg in subgraphs):#if a graph is isomorphic to any other, dont add it
                    subgraphs.append(graph)
    return subgraphs

#example usage
n = 2
subgraphs = generate_subgraphs(n)

#write subgraphs to a textual file
filename = f"subgraphs.txt"
with open(filename, "w") as file:
    file.write(f"n={n}\n")#given number n
    file.write(f"count={len(subgraphs)}\n")#count of all sub-graphs
    for i, subgraph in enumerate(subgraphs, 1):#printing each one in desired form
        file.write(f"# {i}\n")
        for edge in subgraph.edges():
            file.write(f"{edge[0]} {edge[1]}\n")
