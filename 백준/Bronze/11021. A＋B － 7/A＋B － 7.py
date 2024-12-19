import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    a = list(map(int, input().split()))
    print(f"Case #{i + 1}: {a[0] + a[1]}")