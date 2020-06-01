import networkx as nx
import math

def tsp_reader(file):

    G = nx.Graph()

    with open (file, "r") as file:
        for line in file:
            if "NODE_COORD_SECTION" in line:
                break

        for line in file:
            if "EOF" in line:
                break
            
            words = line.split()
            G.add_node(int(words[0]), pos=(float(words[1]), float(words[2])))

        for u in G.nodes():
            for v in G.nodes():
                if u == v:
                    continue
                G.add_edge(u, v, weight=math.sqrt((G.nodes[u]['pos'][0] - G.nodes[v]['pos'][0])**2 + (G.nodes[u]['pos'][1] - G.nodes[v]['pos'][1])**2))

        return G