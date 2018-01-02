import copy
from TdP_collections.graphs.graph import Graph
from Gruppo6_4_TdP.pkg_1.adaptable_heap_priority_queue_max import *


class MyGraph(Graph):

    class Vertex(Graph.Vertex):
        __slots__ = '_cd', '_locator'

        def __init__(self, x):
            """Do not call constructor directly. Use Graph's insert_vertex(x)."""
            super().__init__(x)
            self._cd = 0
            self._locator = None

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
            free_vertices = AdaptableHeapPriorityQueueMax()
            for vertex in self.vertices():
                vertex._locator = free_vertices.add(vertex._cd, vertex)
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

        # scelgo il prossimo vertice sulla base del cover degree maggiore
        try:
            i = free_vertices.remove_max()[1]
        except Empty:
            return min_vcs, kopt
        covered_vertices.append(i)
        k -= 1
        self._fix_neighbours_degree(i, free_vertices, no_solution=True)
        min_vcs, kopt = self._min_vertex_cover_kopt(k=k, uncov=uncov-i._cd, opt=opt, kopt=kopt,
                                                    free_vertices=free_vertices, covered_vertices=covered_vertices,
                                                    uncovered_vertices=uncovered_vertices, min_vcs=min_vcs)
        covered_vertices.pop()
        uncovered_vertices.append(i)
        k += 1
        self._fix_neighbours_degree(i, free_vertices, no_solution=True, covered=False)

        min_vcs, kopt = self._min_vertex_cover_kopt(k=k, uncov=uncov, opt=opt, kopt=kopt,
                                                    free_vertices=free_vertices, covered_vertices=covered_vertices,
                                                    uncovered_vertices=uncovered_vertices, min_vcs=min_vcs)
        uncovered_vertices.pop()
        i._locator = free_vertices.add(i._cd, i)
        return min_vcs, kopt

    def _fix_neighbours_degree(self, i, vertices, solution=None, covered=True, no_solution=False):
        if covered:
            for edge in self.incident_edges(i):
                vertex = edge.opposite(i)
                try:
                    if solution[vertex]:
                        continue
                except KeyError:
                    pass
                except TypeError:
                    pass
                if no_solution:
                    vertex._cd -= 1
                try:
                    vertices.update(vertex._locator, vertex._locator._key -1, vertex)
                except ValueError:
                    return
                except TypeError:
                    pass
        else:
            for edge in self.incident_edges(i):
                vertex = edge.opposite(i)
                try:
                    if solution[vertex]:
                        continue
                except KeyError:
                    pass
                except TypeError:
                    pass
                if no_solution:
                   vertex._cd += 1
                try:
                    vertices.update(vertex._locator, vertex._locator._key+1, vertex)
                except ValueError:
                    return
                except TypeError:
                    pass

    def _bounding(self, uncover, opt, k, kopt):
        lb = max(0, uncover)
        if k < kopt:
            return True
        if lb > opt or uncover == 0:
            return True
        else:
            return False

    def greedy_vertex_cover(self):
        solution = {}
        vertices = AdaptableHeapPriorityQueueMax()

        for vertex in self.vertices():
            vertex._locator = vertices.add(self.degree(vertex), vertex)
        edges_uncovered = self.edge_count()
        while edges_uncovered != 0:
            try:
                max_vertex = vertices.remove_max()[1]
            except Empty:
                return solution
            solution[max_vertex] = max_vertex
            edges_uncovered -= max_vertex._locator._key
            self._fix_neighbours_degree(max_vertex, vertices, solution, True)

        return solution


