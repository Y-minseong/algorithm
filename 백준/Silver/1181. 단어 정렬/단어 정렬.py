def sort2(n):
    n = list(set(s))
    for i in range(len(n)):
        for j in range(len(n) - i - 1):
            if len(n[j]) > len(n[j + 1]) or len(n[j]) == len(n[j + 1]) and n[j] > n[j + 1]:
                n[j], n[j + 1] = n[j + 1], n[j]
    return n

num = int(input())
s = []
for i in range(num):
    s.append(input())
    
sorting = sort2(s)
for i in range(0, len(sorting)):
    print(sorting[i])