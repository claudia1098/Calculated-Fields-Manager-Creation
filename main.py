import networkx as nx
import pickle
import matplotlib.pyplot as plt
import Functions as ft

G = nx.read_gpickle('parts.gpickle')

pos = nx.spring_layout(G)
nx.draw(G, with_labels=True)

plt.show()


print(list(G.nodes))

#ft.program(G)