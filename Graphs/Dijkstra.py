import math
import sys
def minCostPath(dist, path):
    min = sys.maxsize
    for v in range(9):
        if dist[v] < min and path[v] is False:
            min = dist[v]
            vertex = v
    return vertex

def dijkstra(V, graph,src):
    dist = [sys.maxsize] * V
    dist[src] = 0
    path = [False] * V
    for cout in range(V):
        u = minCostPath(dist, path)
        path[u] = True
        for v in range(V):
            if graph[u][v] > 0 and path[v] is False and dist[v] > dist[u] + graph[u][v]:
                dist[v] = dist[u] + graph[u][v]
    for i in range(V):
        print("{}  {}".format(i, dist[i]))

if __name__ == '__main__':
    graph = [
        [0, 4, 0, 0, 0, 0, 0, 8, 0], 
        [4, 0, 8, 0, 0, 0, 0, 11, 0], 
        [0, 8, 0, 7, 0, 4, 0, 0, 2], 
        [0, 0, 7, 0, 9, 14, 0, 0, 0], 
        [0, 0, 0, 9, 0, 10, 0, 0, 0], 
        [0, 0, 4, 14, 10, 0, 2, 0, 0], 
        [0, 0, 0, 0, 0, 2, 0, 1, 6], 
        [8, 11, 0, 0, 0, 0, 1, 0, 7], 
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
    ]
    
    dijkstra(9, graph, 0)