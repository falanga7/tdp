from Gruppo6_4_TdP.pkg_1.my_graph import *


def bridge(g):

    if not isinstance(g, MyGraph):
        raise ValueError("L'oggetto passato non è MyGraph.")

    forest = {}
    bridges = []
    lt = {}
    dt = {}
    time = 0
    parent = {}
    unconnected = False

    for u in g.vertices():
        if u not in forest:
            if unconnected:
                raise ValueError("Il grafo passato non è connesso.")
            forest[u] = None  # u will be the root of a tree
            dfs_bridge(g, u, forest, bridges, lt, dt, time, parent)
            unconnected = True

    return bridges


def dfs_bridge(g, u, discovered, bridges, lt, dt, time, parent):
    dt[u] = time
    lt[u] = time
    time += 1

    for e in g.incident_edges(u):    # for every outgoing edge from u
        v = e.opposite(u)
        try:
            if v not in discovered:        # v is an unvisited vertex
                discovered[v] = e            # e is the tree edge that discovered v
                parent[v] = u
                time = dfs_bridge(g, v, discovered, bridges, lt, dt, time, parent)        # recursively explore from v
                lt[u] = min(lt[u], lt[v])
                if lt[v] > dt[u]:
                    bridges.append(e)
            elif v != parent[u]:
                lt[u] = min(lt[u], dt[v])
        except KeyError:
            continue
    return time
