v, e = map(int, input().split())
visited = [[False] * e for i in range(v)]
graph = []
for i in range(1, v + 1):
    a = input()
    graph.append(a)


            
def dfs(i, j):
    if visited[i][j] == True:
        return
    visited[i][j] = True
    
    if graph[i][j] == '-':
        if j + 1 < e and graph[i][j + 1] == '-' and not visited[i][j + 1]:
            dfs(i, j + 1)
    
    elif graph[i][j] == '|':
        if i + 1 < v and graph[i + 1][j] == '|' and not visited[i + 1][j]:
            dfs(i + 1, j)
            
cnt = 0
for i in range(v):
    for j in range(e):
        if not visited[i][j]:
            cnt += 1
            dfs(i, j)
print(cnt)