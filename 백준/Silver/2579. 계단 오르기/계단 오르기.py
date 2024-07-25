import sys
input = sys.stdin.readline
n = int(input())
stair = [int(input()) for _ in range(n)]


def stairs(stair):
    dp = [0] * (n)
    if n == 1:  # 만약 계단의 수가 1개라면
        return stair[0] 
    elif n == 2: # 만약 계단의 수가 2개라면
        return sum(stair)
    dp[0] = stair[0] 
    dp[1] = stair[0] + stair[1]
    dp[2] = max(stair[0] + stair[2], stair[1] + stair[2])
    # print(dp)
    # print(stair)
    for i in range(3,n): # dp에 저장된 값을 사용하며 점화식 사용.
        dp[i] = max(dp[i - 2] + stair[i], dp[i - 3] + stair[i - 1] + stair[i])
    return dp[-1] # dp에 저장된 마지막 값 리턴.
print(stairs(stair))