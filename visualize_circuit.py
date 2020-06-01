import networkx as nx
import matplotlib.pyplot as plt

# O circuito é uma lista de tuplas de nós. Ex.: [(node1, node2), (node2, node3), (node3, node4)]
def visualize_circuit(G, circuit):
    pos = {}
    for node in G.nodes():
        pos[node] = G.nodes[node]['pos']

    nx.draw(G, pos, with_labels=True, edgelist=circuit)
    plt.show()