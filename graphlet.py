# python3
# -*- coding: utf-8 -*-
# @Author  : bai xin
# @Time    : 2019-02-25 09:51
import networkx as nx
from numpy.linalg import matrix_power
import matplotlib.pyplot as plt
def read_data(fpapth):
    v=[]
    e=[]
    with open(fpapth) as f:
        for line in f.readlines():
            splist=[]
            splist=line.strip('\n').split(",")
            for i in range(3): 
                
                if((splist[i]!=splist[i+1])):
                    v.append(splist[i])
                    e.append((splist[i],splist[i+1]))
                else:
                    splist[i]=splist[i]+"_1"
                    v.append(splist[i])
                    e.append((splist[i],splist[i+1]))
            v.append(splist[4])
    return v,e
def buildgraphlet(vet,edge):
    g = nx.Graph()
    g.clear()
    g.add_nodes_from(vet)
    g.add_edges_from(edge)
    return g
def Adjmatrix(v,e):
    N=len(v)
    matrix = [[0 for i in range(N)] for j in range(N)]
    for each in e:
        matrix[each[0]][each[1]]=1
    return matrix 

def CompFeature(matrix):
    return 

def RWkernel(graphlet):
    A=nx.to_numpy_matrix(graphlet)
    B=matrix_power(A,1)+matrix_power(A,2)+matrix_power(A,3)+matrix_power(A,4)
    return B

def kernelTrick(graphlet1,graphlet2):
    GA=nx.to_numpy_matrix(graphlet1)
    GB=nx.to_numpy_matrix(graphlet2)
    N=len(GA[0])*len(GB[0])
    GC= [[0 for i in range(N)] for j in range(N)]
    for i in range(1,N):
        for j in range(1,N):
            for k in range(1,N):
                for l in range(1,N):
                    GC[(i,k)][(j,l)]=GA[i][j]*GB[k][l]
    return GC

def transGraph(v1,e1,v2,e2):
    vet=[]
    edge=[]
    for i in e1:
        for j in e2:
            vet.append("("+str(e1[i][0])+","+str(e2[j][0])+")")
            vet.append("("+str(e1[i][1])+","+str(e2[j][1])+")")
            edge.append("(("+str(e1[i][0])+","+str(e2[j][0])+")"+", ("+str(e1[i][1])+","+str(e2[j][1])+"))")
    

    return vet,edge
if __name__=="__main__":
    path="G:\\VScode\\leetcode\\annotated-trace.csv"
    v,e=read_data(path)
     
    #v,e=transGraph(a,b,c,d)
    #print(v)
    #print(e)
    '''
    for i in range(len(a)-2):
        if((a[i]!=a[i+1])):
            v.append(str(a[i]))
        else:
            a[i]=str(a[i])+"_1"
            v.append(a[i])
    v.append(a[len(a)-1])
    '''
    #print(g.nodes())
    g=buildgraphlet(v,e)
    pos = nx.spring_layout(g)
    #nx.draw(g,pos,with_labels=True)
    nx.draw(g, pos, node_size=500, node_color="skyblue", with_labels=True)
    plt.show()