from Gruppo6_4_TdP.pkg_1.my_graph import MyGraph


# primo test
grafo1 = MyGraph()

v0 = grafo1.insert_vertex(0)
v1 = grafo1.insert_vertex(1)
v2 = grafo1.insert_vertex(2)
v3 = grafo1.insert_vertex(3)
v4 = grafo1.insert_vertex(4)
v5 = grafo1.insert_vertex(5)
v6 = grafo1.insert_vertex(6)
v7 = grafo1.insert_vertex(7)
v8 = grafo1.insert_vertex(8)
v9 = grafo1.insert_vertex(9)
v10 = grafo1.insert_vertex(10)

grafo1.insert_edge(v0, v1)
grafo1.insert_edge(v1, v2)
grafo1.insert_edge(v2, v3)
grafo1.insert_edge(v3, v4)
grafo1.insert_edge(v2, v5)
grafo1.insert_edge(v5, v6)
grafo1.insert_edge(v2, v7)
grafo1.insert_edge(v7, v8)

vertici = grafo1.greedy_vertex_cover()
vertici = grafo1.min_vertex_cover()

# secondo test
grafo2 = MyGraph()

v0 = grafo2.insert_vertex(0)
v1 = grafo2.insert_vertex(1)
v2 = grafo2.insert_vertex(2)

grafo2.insert_edge(v0, v1)
grafo2.insert_edge(v1, v2)

vertici = grafo2.min_vertex_cover()
print("lol")