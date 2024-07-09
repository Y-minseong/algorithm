def stack(n):
    stk = []
    for i in n:
        a = i.split()
        if a[0] == "push":
            stk.append(a[1])
        elif a[0] == "top":
            if len(stk) == 0:
                print(-1)
            else:
                print(stk[-1])
        elif a[0] == "size":
            print(len(stk))
        elif a[0] == "empty":
            if len(stk) == 0:
                print(1)
            else:
                print(0)
        elif a[0] == "pop":
            if len(stk) == 0:
                print(-1)
            else:
                print(stk.pop())
                
                

num = int(input())
s = []
for i in range(num):
    s.append(input())
stack(s)