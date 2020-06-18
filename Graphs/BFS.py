from collections import deque

def bfs(graph, source):
    q = deque([source])
    visited = [source]
    while q:
        node = q.popleft()
        for vertex in graph[node]:
            if vertex not in visited:
                q.append(vertex)
                visited.append(vertex)
    print(visited)

if __name__ == '__main__':
    graph = {
        'A' : ['B', 'C'],
        'B' : ['D', 'E'],
        'C' : ['F'],
        'D' : [],
        'E' : 'F',
        'F' : []
    }
    bfs(graph, 'A')
    