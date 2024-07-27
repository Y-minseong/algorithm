import sys

# input 값을 받는다.
N = int(sys.stdin.readline())
paper = []
for i in range(N):
    a = list(map(int, sys.stdin.readline().split()))
    paper.append(a)
blue, white = 0, 0

def quarter_square(x, y, n):
    global paper, blue, white
    check = True
    first_color = paper[x][y]
    
    for i in range(x, x+n):
       
        for j in range(y, y+n):
            if paper[i][j] != first_color:
                check = False
                break
        if not check: # 기저조건이 이거인 이유.
            break
                
        
    if check:
        if first_color == 1:
            blue += 1
            
        else:
            white += 1

    else:
        k = n//2
        quarter_square(x, y, k)
        quarter_square(x, y + k, k)
        quarter_square(x + k, y, k)
        quarter_square(x + k, y + k, k)
quarter_square(0, 0, N)
print(white)
print(blue)