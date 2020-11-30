from pygraph.classes.graph import graph
from pygraph.algorithms.traversal import *
from pygraph.mixins.labeling import *
from collections import defaultdict
import heapq

G = graph()

nodes = [1,2,3,4,5]
edges = [[(1,2), 4], [(1,4), 5], [(2,3), 6], [(2,5),3], [(1,3),2], [(3,5),2]]

G.add_nodes(nodes)
#print(G.edges())
for edge in edges:
     G.add_edge(edge[0], edge[1])

def PrimMST(G: graph, v):
    mst = graph()
    mst.add_node(v)
    Edges = []   
    for i in G[v]:
        Edges.append((G.edge_weight((v,i)), v, i))
    heapq.heapify(Edges)

    while Edges:
        cost, start, end = heapq.heappop(Edges)
        if end not in mst:
            mst.add_node(end)
            mst.add_edge((start,end), cost)
            for to_next in G[end]:
                if to_next not in mst:
                    heapq.heappush(Edges, (G.edge_weight((end, to_next)), end, to_next))  
    print(mst)
    return mst      
    
lst = PrimMST(G, 1)
