from collections import deque


def find_indegree(node, graph):
    indegree = dict()
    count = 0
    deleted_node = None
    for _, value in enumerate(graph):
        if node in graph[value]:
            count = count + 1
    return count

if __name__ == '__main__':
    graph = {
        'A' : ['B'],
        'B' : ['C', 'D', 'E'],
        'C' : ['E'],
        'D' : ['E'],
        'E' : ['F'],
        'F' : [],
        'G' : ['D']
    }
    final = []
    queue = deque()
    indegree = dict()
    #Find the indegree of each node
    for key in graph.keys():
        degree = find_indegree(key, graph)
        indegree[key] = degree
        if indegree[key] == 0:
            queue.append(key)
    while queue:
        deleted_node = queue.popleft()
        final.append(deleted_node)
        for i in graph[deleted_node]:
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)
    print(final)
    