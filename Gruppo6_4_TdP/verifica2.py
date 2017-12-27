from Gruppo6_4_TdP.pkg_1.my_graph import MyGraph
from Gruppo6_4_TdP.pkg_2.bridges import *

grafo1 = MyGraph()


v0 = grafo1.insert_vertex(0)
v1 =  grafo1.insert_vertex(1)
v2 = grafo1.insert_vertex(2)
v3 =  grafo1.insert_vertex(3)
v4 = grafo1.insert_vertex(4)
v5 = grafo1.insert_vertex(5)
v6 = grafo1.insert_vertex(6)

grafo1.insert_edge(v0,v1)
grafo1.insert_edge(v0,v4)
grafo1.insert_edge(v3,v4)
grafo1.insert_edge(v1,v3)
grafo1.insert_edge(v1,v2)
grafo1.insert_edge(v4,v5)
grafo1.insert_edge(v0,v6)

bridge(grafo1)