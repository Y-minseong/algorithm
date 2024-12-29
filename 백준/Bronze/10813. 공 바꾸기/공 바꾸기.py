n = list(map(int, input().split()))
N = n[0]
M = n[1]
Ball = []

for i in range(N):
    Ball.append(i + 1)

for i in range(M):
    ball = list(map(int, input().split()))
    a = Ball[ball[0] - 1]
    b = Ball[ball[1] - 1]
    Ball[ball[0] - 1] = b
    Ball[ball[1] - 1] = a
    
print(*Ball)