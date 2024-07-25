n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
d = [[0] * n for _ in range(n)]
dx = [0, 1]
dy = [1, 0]
d[0][0] = 1  # 시작점 초기화
for x in range(n):
    for y in range(n):
        jump = board[x][y]
        if jump == 0:  # 도착
            break
        for i in range(2):
            nx = x + jump * dx[i]
            ny = y + jump * dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                d[nx][ny] += d[x][y]
        # for i in d:
        #     print(i, 'wow')
        # print()
print(d[n-1][n-1])