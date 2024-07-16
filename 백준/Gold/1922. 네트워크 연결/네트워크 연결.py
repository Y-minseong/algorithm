v = int(input())
e = int(input())
parent = [0] * (v + 1)
rank = [0] * (v + 1)  # 유니온 바이 랭크를 위한 랭크 배열

for i in range(1, v + 1):
    parent[i] = i

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, rank, a, b):
    root_a = find_parent(parent, a)
    root_b = find_parent(parent, b)
    if root_a != root_b:
        if rank[root_a] > rank[root_b]:
            parent[root_b] = root_a
        else:
            parent[root_a] = root_b
            if rank[root_a] == rank[root_b]:
                rank[root_b] += 1

edges = []
total_cost = 0

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# 간선을 가중치 기준으로 정렬
edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, rank, a, b)
        total_cost += cost

print(total_cost)
