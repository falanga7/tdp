from TdP_collections.graphs.graph import Graph
from TdP_collections.priority_queue.adaptable_heap_priority_queue import AdaptableHeapPriorityQueue


def emergency_call(g, pos, v, k):
    if not isinstance(g, Graph):
        raise ValueError("G deve essere di tipo Graph")

    if not isinstance(pos, dict):
        raise ValueError("pos deve essere un dizionario")

    if not isinstance(v, Graph.Vertex):
        raise ValueError("v deve essere un oggetto di tipo Vertex")

    d = {}  # d[v] is upper bound from s to v
    cloud = {}  # map reachable v to its d[v] value
    pq = AdaptableHeapPriorityQueue()  # vertex v will have key d[v]
    pqlocator = {}  # map from vertex to its pq locator
    dst = v
    volanti = []
    # for each vertex v of the graph, add an entry to the priority queue, with
    # the source having distance 0 and all others having infinite distance
    for v in g.vertices():
        if v is dst:
            d[v] = 0
        else:
            d[v] = float('inf')  # syntax for positive infinity
        pqlocator[v] = pq.add(d[v], v)  # save locator for future updates
    emergency = k
    while not pq.is_empty():
        key, u = pq.remove_min()
        cloud[u] = key  # its correct d[u] value
        try:
            if emergency == 0:
                if not volanti:
                    raise ValueError("Nessun volante è disponibile per assistere l'incidente.")
                else:
                    return volanti
            elif pos[u] and emergency != 0:
                volanti.append(pos[u])
                emergency -= 1
        except KeyError:
            pass
        del pqlocator[u]  # u is no longer in pq
        for e in g.incident_edges(u, outgoing=False):  # outgoing edges (u,v)
            v = e.opposite(u)
            if v not in cloud:
                # perform relaxation step on edge (u,v)
                wgt = e.element()
                if d[u] + wgt < d[v]:  # better path to v?
                    d[v] = d[u] + wgt  # update the distance
                    pq.update(pqlocator[v], d[v], v)  # update the pq entry
    if not volanti:
        raise ValueError("Nessun volante è disponibile per assistere l'incidente.")

    return volanti




