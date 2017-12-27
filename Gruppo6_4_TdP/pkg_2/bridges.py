from TdP_collections.graphs.dfs import DFS
from TdP_collections.graphs.graph import Graph
import time

time = 0

def bridge(graph):
    if not isinstance(graph, Graph):
        raise ValueError("Il parametro passato deve essere un'istanza di Graph")
    visited = {}
    disc = {}
    low = {}
    parent = {}
    #mark all vertices as not visited
    #initialize parent e visited arrays
    for vertex in graph.vertices():
        parent[vertex] = None
        visited[vertex] = False
    #Call the recursive helper function to find Bridges in DFS tree rooted with vertex
    for vertex in graph.vertices():
        if visited[vertex] == False:
            dfs_brigde(graph, vertex, visited, disc, low, parent)


def dfs_brigde(graph, vertex, visited, disc, low, parent):

    # Mark the current node as visited
    visited[vertex] = True
    # Initialize discovery time and low value
    global time
    disc[vertex] = low[vertex] = time
    time += 1

    #Go through all vertices aadjacent to this
    for edge in graph.incident_edges(vertex):
        neighbor = edge.opposite(vertex)
        # If neighbor is not visited yet, then recur for it
        if visited[neighbor] == False:
            parent[neighbor] = vertex
            dfs_brigde(graph, neighbor, visited, disc, low, parent)

            #Check if the subtree rooted with neighbor has a connection to one of the ancestors of vertex
            if low[vertex] > low[neighbor]:
                low[vertex] = low[neighbor]
            #If the lowest vertex reachable from subtree under neighbor is  below vertex in DFS tree, then neighbor-vertex is a brige
            if low[neighbor] > disc[vertex]:
                print("Bridge:",vertex,neighbor)

        #// Update low value of u for parent function calls.
        elif neighbor != parent[vertex]:
            if low[vertex] > disc[neighbor]:
                low[vertex] = disc[neighbor]
