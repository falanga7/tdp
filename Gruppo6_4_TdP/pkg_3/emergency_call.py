from TdP_collections.graphs.graph import Graph
from TdP_collections.graphs.shortest_paths import shortest_path_lengths
from TdP_collections.priority_queue.sorted_priority_queue import SortedPriorityQueue


def emergency_call(G, pos, v, k):

    if not isinstance(G, Graph):
        raise ValueError("G deve essere di tipo Graph")

    if not isinstance(pos, dict):
        raise ValueError("pos deve essere un dizionario")

    if not isinstance(v, Graph.Vertex):
        raise ValueError("v deve essere un oggetto di tipo Vertex")

    volanti = {}
    queue = SortedPriorityQueue()
    soluzione = list()

    for volante, partenza in pos.items():
        volanti[volante] = shortest_path_lengths(G, partenza)
        for key,value in volanti[volante].items():
            if key.element() == v.element() and isinstance(value, int):
                queue.add(value, volante)
                pass

    if not queue.is_empty():
        for i in range(k):
            soluzione.append(queue.remove_min())
    else:
        raise ValueError("Nessuna volante può raggiungere l'incidente")

    return soluzione