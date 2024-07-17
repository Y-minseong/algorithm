import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

v = int(input())
graph = [[] for i in range(v + 1)]
for i in range(v - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
visited = [False] * (v + 1)
    
def dfs(node):
    for i in graph[node]:
        if visited[i] == 0:
            visited[i] = node
            dfs(i)

dfs(1)

for i in range(2, v + 1):
    print(visited[i])