import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("petit2.csv")
Graphtype = nx.Graph()
G = nx.from_pandas_edgelist(df, source='bo', target='rbo', edge_attr='f', create_using=nx.DiGraph())

nx.draw(G, with_labels = True)

plt.show()