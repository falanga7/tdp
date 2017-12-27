import copy
from TdP_collections.graphs.graph import Graph


class MyGraph(Graph):

    class Vertex(Graph.Vertex):
        __slots__ = '_cd'

        def __init__(self, x):
            """Do not call constructor directly. Use Graph's insert_vertex(x)."""
            super().__init__(x)
            self._cd = 0

    def insert_edge(self, u, v, x=None):
        """Insert and return a new Edge from u to v with auxiliary element x.

        Raise a ValueError if u and v are not vertices of the graph.
        Raise a ValueError if u and v are already adjacent.
        """
        super().insert_edge(u, v, x)
        u._cd += 1
        v._cd += 1

    def min_vertex_cover(self):
        min_vcs = self._min_vertex_cover_kopt()
        return min_vcs[0]

    def _min_vertex_cover_kopt(self, **params):
        """ Inizializzazione
            k = numero di vertici da coprire
            uncov = numero di archi da coprire
            opt = minimo numero di archi scoperti trovati finora
            free_vertices = vertici marcati come free, ancora da esplorare,
            o liberi a causa del backtracking
            covered_vertices
            covered_vertices = vertici marcati come coperti
            uncovered_vertices = vertici marcati come scoperti
            kopt = rappresenta i vertici rimanenti da coprire nella soluzione ottima
            min_vcs = rappresenta l'insieme di copertura minimo trovato finora.
            """
        # prima inizializzazione dei parametri
        if not params:
            k = self.vertex_count()
            uncov = self.edge_count()
            opt = uncov
            free_vertices = []
            for vertex in self.vertices():
                free_vertices.append(vertex)
            covered_vertices = []
            uncovered_vertices = []
            min_vcs = []
            kopt = 0

        elif len(params) != 8:
            raise ValueError("Il metodo è stato chiamato con un numero di parametri non previsto.")

        # Inizializzazione dei parametri passati alle successive chiamate ricorsive.
        else:
            k = params["k"]
            uncov = params["uncov"]
            opt = params["opt"]
            free_vertices = params["free_vertices"]
            covered_vertices = params["covered_vertices"]
            uncovered_vertices = params["uncovered_vertices"]
            min_vcs = params["min_vcs"]
            kopt = params["kopt"]

        # caso in cui ho coperto tutti i vertici
        if k == 0:
            min_vcs = copy.deepcopy(covered_vertices)
            return min_vcs, kopt

        if uncov < opt:
            opt = uncov
            # ho trovato una soluzione ottima
            if uncov == 0:
                # è migliore della precedente soluzione ottima trovata?
                if k > kopt:
                    kopt = k
                    min_vcs = copy.deepcopy(covered_vertices)
                    return min_vcs, kopt

        if self._bounding(uncov, opt, k, kopt):
            return min_vcs, kopt

        def cover_degree(vertex):
            return vertex._cd
        # scelgo il prossimo vertice sulla base del cover degree maggiore
        free_vertices.sort(key=cover_degree)
        try:
            i = free_vertices.pop()
        except IndexError:
            return min_vcs, kopt
        covered_vertices.append(i)
        k -= 1
        self._fix_neighbours_degree(i)
        min_vcs, kopt = self._min_vertex_cover_kopt(k=k, uncov=uncov-i._cd, opt=opt, kopt=kopt,
                                                    free_vertices=free_vertices, covered_vertices=covered_vertices,
                                                    uncovered_vertices=uncovered_vertices, min_vcs=min_vcs)
        covered_vertices.pop()
        uncovered_vertices.append(i)
        k += 1
        self._fix_neighbours_degree(i, False)

        min_vcs, kopt = self._min_vertex_cover_kopt(k=k, uncov=uncov, opt=opt, kopt=kopt,
                                                    free_vertices=free_vertices, covered_vertices=covered_vertices,
                                                    uncovered_vertices=uncovered_vertices, min_vcs=min_vcs)
        uncovered_vertices.pop()
        free_vertices.append(i)
        return min_vcs, kopt

    def _fix_neighbours_degree(self, i, covered=True):
        if covered:
            for edge in self.incident_edges(i):
                edge.opposite(i)._cd -= 1
        else:
            for edge in self.incident_edges(i):
                edge.opposite(i)._cd += 1

    def _bounding(self, uncover, opt, k, kopt):
        lb = max(0, uncover)
        if k < kopt:
            return True
        if lb > opt or uncover == 0:
            return True
        else:
            return False

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


