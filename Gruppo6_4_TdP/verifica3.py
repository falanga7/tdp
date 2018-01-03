from TdP_collections.graphs.graph import Graph
from Gruppo6_4_TdP.pkg_3.emergency_call import emergency_call
import string
from Gruppo6_4_TdP.util import randList

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

# polizia = {v4: 1, v5: 2, v6: 3}

polizia = {1: v4, 2: v5, 3: v6}

volanti = emergency_call(grafo1, polizia, v5, 2)

print("Volanti:")
print(volanti)


print("Test con city_map.text:")
grafo6 = Graph(True)
city_file = open("city_map.txt", "r")
vertices_city = {}
for i in range(1, 71):
    vertex_label = i
    vertices_city[vertex_label] = grafo6.insert_vertex(vertex_label)
lines = city_file.readlines()

for i in range(2, 368):
    src = lines[i].split()[0]
    dst = lines[i].split()[1]
    wt = lines[i].split()[2]
    grafo6.insert_edge(vertices_city[int(src)], vertices_city[int(dst)], int(wt))

posizione_volanti = randList(1, len(vertices_city)-1, 10)
volanti = {}
id_volante = 1
for i in posizione_volanti:
    volanti[id_volante] = vertices_city[i]
    id_volante += 1
print("Posizione iniziale volanti")
for id_volante,pos_volante in volanti.items():
    print("Id volante:",id_volante," - Posizione: ",pos_volante)

incidente =  vertices_city[randList(1, len(vertices_city)-1, 1)[0]]
volanti = emergency_call(grafo6, volanti, incidente, 5)

print("Si è verificato un incidente all'incrocio N°: ",incidente)
print("Volanti chiamate:")
print(volanti)