import math
def prim(v, graph):
    vertex = 0
    MST = []
    edges = []
    visited = []
    minEdge = [None, None, math.inf]
    while len(MST) != v:
        visited.append(vertex)
        for i in range(0,v):
            if graph[vertex][i] != 0:
                edges.append([vertex,i,graph[vertex][i]])
        for i in range(len(edges)):
            if edges[i][2] < minEdge[2] and ((edges[i][1] in visited) is False):
                minEdge = edges[i]
        if minEdge == [None, None, math.inf]:
            return MST
        edges.remove(minEdge)
        MST.append(minEdge)
        vertex = minEdge[1]
        minEdge = [None, None, math.inf]

if __name__ == '__main__':
    graph = [
        [0,7,3,0,0],
        [7,0,4,9,11],
        [3,4,0,10,0],
        [0,9,10,0,0],
        [0,11,0,0,0]
    ]
    print(prim(5, graph))