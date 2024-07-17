import sys
input = sys.stdin.read

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

data = input().split()
v = int(data[0])
e = int(data[1])
parent = [i for i in range(v + 1)]
rank = [0] * (v + 1)

edges = []
total_cost = 0
index = 2

for _ in range(e):
    a = int(data[index])
    b = int(data[index + 1])
    cost = int(data[index + 2])
    edges.append((cost, a, b))
    index += 3

# 간선을 가중치 기준으로 정렬
edges.sort()

for cost, a, b in edges:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, rank, a, b)
        total_cost += cost

print(total_cost)
