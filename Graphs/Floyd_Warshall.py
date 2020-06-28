import sys

def Warshall(graph, V):
    dist = graph
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    print(dist)

if __name__ == '__main__':
    graph = [
        [0, 3, 0 ,5],
        [2 ,0 ,0, 4],
        [0, 1, 0, 0],
        [0, 0, 2, 0]
    ]
    for i in range(4):
        for j in range(4):
            if graph[i][j] == 0 and i != j:
                graph[i][j] = sys.maxsize
    Warshall(graph, 4)