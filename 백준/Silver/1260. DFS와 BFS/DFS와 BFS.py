from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end = ' ')
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            
def bfs(graph, start, visi):
    queue = deque([start])
    visi[start] = True
    
    while queue:
        v = queue.popleft()
        print(v, end = " ")
        
        for i in graph[v]:
            if not visi[i]:
                queue.append(i)
                visi[i] = True
            
vertex, e, v = map(int, input().split())
graph = [[] for _ in range(vertex + 1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for edges in graph:
    edges.sort()
    
visited = [False] * (vertex + 1)
dfs(graph, v, visited)
print()
visited = [False] * (vertex + 1)
bfs(graph, v, visited)

