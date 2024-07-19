from collections import deque
def bfs(graph, start, k):
    distances = [-1] * (len(graph) + 1)
    distances[start] = 0

    queue = deque([start])

    while queue:
        v = queue.popleft()
        for neighbor in graph[v]:
            if distances[neighbor] == -1:
                distances[neighbor] = distances[v] + 1
                queue.append(neighbor)
    result = []
    for i in range(len(distances)):
        if distances[i] == k:
            result.append(i)
    return result
n, m, k, x = map(int, input().split())
graph = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

result = bfs(graph, x, k)

if result:
    for city in sorted(result):
        print(city)
else:
    print(-1)