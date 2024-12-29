n = list(map(int, input().split()))
N = n[0]
M = n[1]
Ball = []
for i in range(N):
    Ball.append(0)
    
for i in range(M):
    ball = list(map(int, input().split()))
    for j in range(ball[0] - 1, ball[1]):
        Ball[j] = ball[2]
    
print(*Ball)