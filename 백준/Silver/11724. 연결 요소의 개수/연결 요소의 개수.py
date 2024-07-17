v, e = map(int, input().split())
visited = [False] * (v + 1)
graph = [[] for i in range(v + 1)]

for i in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(v + 1):
    graph[i].sort()

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            
cnt = 1
            
dfs(graph, 1, visited)

            
for i in range(1, len(visited)):
    if visited[i] == False:
        cnt +=1
        dfs(graph, i, visited)
print(cnt)

