visited = []

def dfs_recursive(graph, start):
    global visited
    if start not in visited:
        visited.append(start)
        for node in graph[start]:
            dfs_recursive(graph, node)

#Non-recursive approach
def dfs(graph, start):
    global visited
    stack = [start]
    visited = [start]
    while stack:
        node = stack[-1]
        if node not in visited:
            visited.append(node)
        flag = True
        for next in graph[node]:
            if next not in visited:
                stack.append(next)
                flag = False
                break
        if flag:
            stack.pop()

if __name__ == '__main__':
    graph = {
        'A' : ['B', 'C', 'D'],
        'B' : ['E'],
        'C' : ['B', 'G'],
        'D' : ['C', 'G'],
        'E' : ['C', 'F'],
        'F' : ['C', 'H'],
        'G' : ['F', 'H', 'I'],
        'H' : ['E', 'I'],
        'I' : ['F']
    }
    dfs_recursive(graph, "H")
    print(visited)
    #visited.clear()
    #dfs(graph, 'H')
    #print(visited)