def bellmanFord(graph, V, src):
    dist = [float('INF')] * V
    dist[src] = 0
    for _ in range(V - 1):
        for source, destination, cost in graph:
            if dist[source] != float('INF') and dist[destination] > dist[source] + cost:
                dist[destination] = dist[source] + cost
    
    for source, destination,cost in graph:
        if dist[source] != float('INF') and dist[destination] > dist[source] + cost:
            print("Negative weight cycle detected.")
            return
    
    for i, val in enumerate(dist):
        print("{} {}".format(i, val))
    

if __name__ == '__main__':
    graph = [
        [0, 1, -1],
        [0, 2, 4],
        [1, 2, 3],
        [1, 3, 2],
        [1, 4, 2],
        [3, 2, 5],
        [3, 1, 1],
        [4, 3, -3]
    ]
    bellmanFord(graph, 5, 0)