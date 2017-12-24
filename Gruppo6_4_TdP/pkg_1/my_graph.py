import copy
from TdP_collections.graphs.graph import Graph


class MyGraph(Graph):

    class Vertex(Graph.Vertex):
        __slots__ = '_cd', '_label'

        def __init__(self, x):
            """Do not call constructor directly. Use Graph's insert_vertex(x)."""
            super().__init__(x)
            self._cd = 0
            self._label = 0

    def insert_edge(self, u, v, x=None):
        """Insert and return a new Edge from u to v with auxiliary element x.

        Raise a ValueError if u and v are not vertices of the graph.
        Raise a ValueError if u and v are already adjacent.
        """
        super().insert_edge(u, v, x)
        u._cd += 1

    def min_vertex_cover(self, k=None, uncov=None, opt=None):
        if k is None and uncov is None and opt is None:
            k = self.vertex_count()
            uncov = self.edge_count()
            opt = self.edge_count()
        if k == 0:
            if uncov < opt:
                opt = uncov
        if
        i = next(self.vertices())
        i._label = 2
        k -= 1
        for edge in self.incident_edges(i):
            edge.opposite(i)._cd -= 1
        self.min_vertex_cover(k, uncov-i._cd, opt)
        i._label = 1
        k += 1
        for edge in self.incident_edges(i):
            edge.opposite(i)._cd += 1

        self.min_vertex_cover(k, uncov, opt)
        i._label = 0



    def delete_edge(self, u, v):
        """Insert and return a new Edge from u to v with auxiliary element x.

        Raise a ValueError if u and v are not vertices of the graph.
        Raise a ValueError if u and v are already adjacent.
        """
        del self._outgoing[u][v]
        del self._incoming[v][u]

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


