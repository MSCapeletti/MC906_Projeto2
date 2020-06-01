import networkx as nx

import instanceReader
import random_circuit as rc
import visualize_circuit as vc

G = instanceReader.tsp_reader("att48.tsp")

random_solution = rc.random_circuit(G)

vc.visualize_circuit(G, random_solution)