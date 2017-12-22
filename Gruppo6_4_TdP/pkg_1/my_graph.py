import copy
from TdP_collections.graphs.graph import Graph


class MyGraph(Graph):

    def delete_edge(self, u, v):
        """Insert and return a new Edge from u to v with auxiliary element x.

        Raise a ValueError if u and v are not vertices of the graph.
        Raise a ValueError if u and v are already adjacent.
        """
        del self._outgoing[u][v]
        del self._incoming[v][u]


    def min_vertex_cover(self):
        pass

    def greedy_vertex_cover(self):

        my_graph = copy.deepcopy(self)

        solution = []
        vertices = []

        for vertex in my_graph.vertices():
            vertices.append(vertex)
        vertices.sort(key=my_graph._sort_desc_degree)

        while my_graph.edge_count() != 0:
            max_vertex = vertices.pop()
            solution.append(max_vertex)

            while my_graph.degree(max_vertex) != 0:
                incident = my_graph.incident_edges(max_vertex).__next__() #trovare un modo più elegante
                opposite = incident.opposite(max_vertex)

                try:
                    vertices.remove(opposite)
                except:
                    continue
                finally:
                    my_graph.delete_edge(max_vertex, opposite)


        return solution




    def _sort_desc_degree(self, vertex):

        return self.degree(vertex)


