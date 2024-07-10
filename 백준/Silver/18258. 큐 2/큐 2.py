from collections import deque

def que(n):
    q = deque()
    for i in n:
        b = i.split(' ')
        if b[0] == "push":
            q.append(b[1])
        elif b[0] == "front":
            if len(q) == 0:
                print(-1)
            else:
                print(q[0])
        elif b[0] == "back":
            if len(q) == 0:
                print(-1)
            else:
                print(q[-1])
        elif b[0] == "size":
            print(len(q))
        elif b[0] == "empty":
            if len(q) == 0:
                print(1)
            else:
                print(0)
        elif b[0] == "pop":
            if len(q) == 0:
                print(-1)
            else:
                print(q.popleft())
                
num = int(input())
a = []
for i in range(num):
    a.append(input())
que(a)
    