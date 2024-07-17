v = int(input())
e = int(input())
visited = [False] * (v + 1)
graph = [[] for i in range(v + 1)]
for i in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for edge in range(v + 1):
    graph[edge].sort()

def dfs(graph, v, visited):
    cnt = 0
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
    for i in range(2, len(visited)):
        if visited[i] == True:
            cnt += 1
        else:
            continue
    return cnt 
print(dfs(graph, 1, visited))