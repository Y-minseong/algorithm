import heapq

def dijkstra(N, graph, start, end):
    distances = [float('inf')] * (N + 1)
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances[end]

N = int(input())
M = int(input())
graph = [[] for i in range(N + 1)]
for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    
start_node, end = map(int, input().split())

distances = dijkstra(N, graph, start_node, end)
print(distances)
