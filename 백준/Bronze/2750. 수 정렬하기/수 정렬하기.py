def sort(n):  # ex. [5,4,3,2,1]
    for i in range(len(n)):
        for j in range(0, len(n) - i - 1):
            if n[j] > n[j+1]:
                temp = n[j]
                n[j] = n[j+1]
                n[j+1] = temp
    return n
    






num = int(input())
s = []
for i in range(num):
    s.append(int(input()))

for i in range(len(sort(s))):
    print(sort(s)[i])