import networkx as nx
import random

def random_circuit(G):
    node_list = list(G.nodes())
    num_of_nodes = len(node_list)

    sol_nodes = []
    while len(sol_nodes) < num_of_nodes:
        next_node = random.choice(node_list)
        node_list.remove(next_node)
        sol_nodes.append(next_node)

    sol_edges = [(sol_nodes[-1], sol_nodes[0])]
    prev = sol_nodes[0]
    for node in sol_nodes:
        if node == prev:
            continue
        sol_edges.append((prev, node))
        prev = node

    return sol_edges