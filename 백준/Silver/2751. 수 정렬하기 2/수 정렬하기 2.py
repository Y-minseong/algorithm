s = int(input())
n = []
for i in range(s):
    n.append(int(input()))



def sort1(x):
    x.sort()
    return x


for i in range(len(sort1(n))):
    print(n[i])