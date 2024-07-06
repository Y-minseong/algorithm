num = int(input())
for z in range(num):
    n, s = input().split()
    for i in range(len(s)):
        print(s[i] * int(n), end = '')
        
    print()
    #임채승 하스 짐