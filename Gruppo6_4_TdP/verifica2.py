from Gruppo6_4_TdP.pkg_2.bridge import *

# test primo grafo
grafo1 = MyGraph()

v0 = grafo1.insert_vertex(0)
v1 = grafo1.insert_vertex(1)
v2 = grafo1.insert_vertex(2)
v3 = grafo1.insert_vertex(3)
v4 = grafo1.insert_vertex(4)
v5 = grafo1.insert_vertex(5)
v6 = grafo1.insert_vertex(6)

grafo1.insert_edge(v0, v1)
grafo1.insert_edge(v0, v2)
grafo1.insert_edge(v1, v2)
grafo1.insert_edge(v1, v6)
grafo1.insert_edge(v1, v3)
grafo1.insert_edge(v3, v5)
grafo1.insert_edge(v1, v4)
grafo1.insert_edge(v4, v5)

print("Bridge del primo grafo:")
bridges = bridge(grafo1)
for edge in bridges:
    print(edge)

# test secondo grafo

grafo2 = MyGraph()

v0 = grafo2.insert_vertex(0)
v1 = grafo2.insert_vertex(1)
v2 = grafo2.insert_vertex(2)
v3 = grafo2.insert_vertex(3)
v4 = grafo2.insert_vertex(4)

grafo2.insert_edge(v0, v1)
grafo2.insert_edge(v0, v2)
grafo2.insert_edge(v1, v2)
grafo2.insert_edge(v0, v3)
grafo2.insert_edge(v3, v4)

print("Bridge del secondo grafo:")
bridges = bridge(grafo2)
for edge in bridges:
    print(edge)

# test terzo grafo

grafo3 = MyGraph()

v0 = grafo3.insert_vertex(0)
v1 = grafo3.insert_vertex(1)
v2 = grafo3.insert_vertex(2)
v3 = grafo3.insert_vertex(3)


grafo3.insert_edge(v0, v1)
grafo3.insert_edge(v1, v2)
grafo3.insert_edge(v2, v3)


print("Bridge del terzo grafo:")
bridges = bridge(grafo3)
for edge in bridges:
    print(edge)

# test quarto grafo

# grafo4 = MyGraph()
#
# v0 = grafo4.insert_vertex(0)
# v1 = grafo4.insert_vertex(1)
# v2 = grafo4.insert_vertex(2)
# v3 = grafo4.insert_vertex(3)
#
#
# grafo4.insert_edge(v0, v1)
# grafo4.insert_edge(v2, v3)
#
#
# print("Bridge del quarto grafo:")
# bridges = bridge(grafo4)
# for edge in bridges:
#     print(edge)

# test quinto grafo

grafo5 = MyGraph()

v0 = grafo5.insert_vertex(0)
v1 = grafo5.insert_vertex(1)
v2 = grafo5.insert_vertex(2)
v3 = grafo5.insert_vertex(3)
v4 = grafo5.insert_vertex(4)


grafo5.insert_edge(v0, v1)
grafo5.insert_edge(v0, v2)
grafo5.insert_edge(v0, v3)
grafo5.insert_edge(v0, v4)
grafo5.insert_edge(v1, v2)
grafo5.insert_edge(v2, v3)
grafo5.insert_edge(v2, v4)

print("Bridge del quinto grafo:")
bridges = bridge(grafo5)
for edge in bridges:
    print(edge)
