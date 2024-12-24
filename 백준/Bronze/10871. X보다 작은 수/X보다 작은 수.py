N, X = list(map(int, input().split()))

num = list(map(int, input().split()))
A = []
for i in range(len(num)):
    if (num[i] < X):
        A.append(num[i])
print(*A)