
parent = {}
def makeSet(N):
    global parent
    for i in range(N):
        parent[i] = i

def find(k):
    global parent
    if parent[k] == k:
        return k
    return find(parent[k])
    
def union(a,b):
    global parent
    x = find(a)
    y = find(b)
    parent[x] = y
    
    
def kruskal(v, graph):
    MST = []
    makeSet(v)
    index = 0
    while len(MST) != v-1:
        (s,d,w) = graph[index]
        index+=1
        x=find(s)
        y=find(d)
        if x!=y:
            MST.append([s,d,w])
            union(x,y)
    print(MST)

if __name__ == '__main__':
    graph = [
        [0,1,7],
        [0,2,6],
        [0,3,1],
        [1,2,8],
        [2,3,5],
        [2,4,3],
        [3,4,4],
        [3,5,5],
        [4,5,2]
    ]
    graph = sorted(graph, key = lambda item:item[2])
    kruskal(6, graph)
    