import sys
input = sys.stdin.readline
n = int(input())
paper = []
for i in range(n):
    a = list(map(int, input().split()))
    paper.append(a)
blue, white = 0, 0

def cut_paper(x, y, n):
    global paper, blue, white
    start_paper = paper[x][y]
    check = True
    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j] != start_paper:
                check = False
                break
        if not check:
            break
    
    if check:
        if start_paper == 1:
            blue += 1
        else:
            white += 1
    else:
        k = n // 2
        cut_paper(x, y, k)
        cut_paper(x, y + k, k)
        cut_paper(x + k, y, k)
        cut_paper(x + k, y + k, k)

cut_paper(0, 0, n)
print(white)
print(blue)