from collections import deque
N , M = map(int, input().split())
board = [input().strip() for _ in range(N)]
dx = (1, 0, -1, 0) # x 행렬
dy = (0, 1, 0, -1) # y 행렬


def bfs(): # 함수 실행
    visited = [[False] * M for _ in range(N)] # 방문 기록 초기화
    visited[0][0] = True # [0][0]을 방문 입력
    dq = deque() # 큐 생성
    dq.append((0, 0, 1)) # y값과 x값 그리고 카운트 append()
    while dq: # 큐가 빌 때까지 실행
        y, x, d = dq.popleft() # 큐에서 추출
        
        if y == N - 1 and x == M - 1: # 기저 조건
            return d
        
        for i in range(4):
            ny = y + dy[i] # 현재 위치한 행렬 옮기기
            nx = x + dx[i]
            # 행렬을 넘지 않는지, 1로 되어있는지 그리고 방문기록이 없는지 확인
            if 0 <= ny < N and 0 <= nx < M and board[ny][nx] == '1' and not visited[ny][nx]:
                visited[ny][nx] = True # 조건문이 통과됬다면 True로 교체
                dq.append((ny, nx, d + 1)) # 큐에 추가
    return - 1
                
print(bfs())
     

