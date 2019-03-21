import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import csv
import numpy

# Ignore matplotlib warnings
import warnings
warnings.filterwarnings("ignore")

# input_data = pd.read_csv('annotated-trace.csv')
# print (input_data.values)

G = nx.DiGraph()

with open('annotated-trace.csv', 'rt') as tsvin:
	tsvin = csv.reader(tsvin, delimiter=',')

	for row in tsvin:
		srcIP = row[0]
		dstIP = row[1]
		protocol = row[2]
		sPort = row[3]
		dPort = row[4]
		state = row[5]

		G.add_edge(srcIP, protocol)
		G.add_edge(protocol, dstIP)
		G.add_edge(dstIP, sPort)
		G.add_edge(sPort, dPort)
		G.add_edge(dPort, state)

		# print(G.edges())

# print("Edges of graph: ")
# print(G.edges())

pos = nx.spring_layout(G)
nx.draw(G, pos, node_size=500, node_color="skyblue", with_labels=True)
plt.show()
