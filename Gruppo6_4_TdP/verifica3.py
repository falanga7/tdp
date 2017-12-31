from TdP_collections.graphs.graph import Graph
from Gruppo6_4_TdP.pkg_3.emergency_call import emergency_call

grafo1 = Graph(True)

v0 = grafo1.insert_vertex(0)
v1 = grafo1.insert_vertex(1)
v2 = grafo1.insert_vertex(2)
v3 = grafo1.insert_vertex(3)
v4 = grafo1.insert_vertex(4)
v5 = grafo1.insert_vertex(5)
v6 = grafo1.insert_vertex(6)

grafo1.insert_edge(v1, v0, 1)
grafo1.insert_edge(v0, v4, 4)
grafo1.insert_edge(v3, v4, 3)
grafo1.insert_edge(v1, v3, 10)
grafo1.insert_edge(v1, v2, 1)
grafo1.insert_edge(v4, v5, 2)
grafo1.insert_edge(v5, v6, 1)
grafo1.insert_edge(v2, v6, 1)
grafo1.insert_edge(v6, v4, 1)

polizia = {1: v4, 2: v5, 3: v6}

volanti = emergency_call(grafo1, polizia, v4, 2)

print("Volanti")
print(volanti)
