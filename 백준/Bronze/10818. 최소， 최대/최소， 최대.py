N = int(input())
num = list(map(int, input().split()))
a = []

a.append(min(num))
a.append(max(num))
print(*a)