import networkx as nx
import matplotlib.pyplot as plt
# from networkx.drawing.nx_agraph import graphviz_layout

# G=nx.DiGraph()
# for i in range(1,16):
# 	G.add_node(i)

# nodeLabel = {
# 	1 : "12.124.65.34",
# 	2 : "17",
# 	3 : "12.124.65.33",
# 	4 : "138",
# 	5 : "138",

# 	6 : "12.124.65.35",
# 	7 : "12.124.65.37",
# 	8 : "80",
# 	9 : "80",

# 	10 : "6",
# 	11 : "12.124.65.36",
# 	12 : "167",

# 	13 : "12.124.65.36",
# 	14 : "443",
# 	15 : "443"
# }

# G.add_edges_from([
# 	(1, 2),
# 	(2, 3),
# 	(3, 4),
# 	(4, 5),

# 	(6, 2),
# 	(2, 7),
# 	(7, 8),
# 	(8, 9),

# 	(6, 10),
# 	(10, 11),
# 	(11, 12),
# 	(12, 9),

# 	(13, 10),
# 	(10, 7),
# 	(7, 14),
# 	(14, 15),
# ])

# H=nx.relabel_nodes(G,nodeLabel)

# print("Nodes of graph: ")
# print(H.nodes())
# print("Edges of graph: ")
# print(H.edges())
# nx.draw(H,with_labels=True)
# # # plt.savefig("path_graph_cities.png")
# plt.show()

class srcIP:
	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return self.name

class protocol:
	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return self.name

class dstIP:
	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return self.name

class sPort:
	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return self.name

class dPort:
	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return self.name

src1 = srcIP("12.124.65.34")
src2 = srcIP("12.124.65.35")
src3 = srcIP("12.124.65.36")

pro1 = protocol("17")
pro2 = protocol("6")

dst1 = dstIP("12.124.65.33")
dst2 = dstIP("12.124.65.36")
dst3 = dstIP("12.124.65.37")

sP1 = sPort("138")
sP2 = sPort("80")
sP3 = sPort("167")
sP4 = sPort("443")

dP1 = dPort("138")
dP2 = dPort("80")
dP3 = dPort("443")

G = nx.DiGraph()
G.add_nodes_from([src1, src2, src3, pro1, pro2, dst1, dst2, dst3,
sP1, sP2, sP3, sP4, dP1, dP2, dP3])
G.add_edges_from([
	(src1, pro1),
	(pro1, dst1),
	(dst1, sP1),
	(sP1, dP1),

	(src2, pro1),
	(pro1, dst3),
	(dst3, sP2),
	(sP2, dP2),

	(src2, pro2),
	(pro2, dst2),
	(dst2, sP3),
	(sP3, dP2),

	(src3, pro2),
	(pro2, dst3),
	(dst3, sP4),
	(sP4, dP3),
])

print("Nodes of graph: ")
print(G.nodes())
print("Edges of graph: ")
print(G.edges())
pos = nx.sring_layout(G)
nx.draw(G, pos, node_size=500, node_color="skyblue", with_labels=True)
plt.show()