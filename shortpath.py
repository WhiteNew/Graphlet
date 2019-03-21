# python3
# -*- coding: utf-8 -*-
# @Author  : bai xin
# @Time    : 2019-02-25 08:51
import numpy as np
import networkx as nx
from numpy.linalg import matrix_power
inf=-999999
def floydAlogrithm(graphlet,distance):
    A=nx.to_numpy_matrix(graphlet)
    n=len(A[0])
    cost = [[0 for i in range(n)] for j in range(n)]
    for i in range(1,n):
        for j in range(1,n):
            if (A[i][j]==1) and (i!=j):
                cost[i][j]=distance[i][j]
            else:
                if(i==j):
                    cost[i][j]=0
                else:
                    cost[i][j]=inf
    for k in range(1,n):
        for i in range(1,n):
            for j in range(1,n):
                if(cost[i][k]+cost[k][j]<cost[i][j]<cost[i][j]):
                    cost[i][j]=cost[i][k]+cost[k][j]
    return cost
def buildgraphlet(vet,edge):
    g = nx.Graph()
    g.clear()
    g.add_nodes_from(vet)
    g.add_edges_from(edge)
    return g
def Distancematrix(v,e):
    N=len(v)
    distance = [[0 for i in range(N)] for j in range(N)]
    for each in e:
        distance[each[0]][each[1]]=1
    return distance 
