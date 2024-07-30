def recursion(s, l ,r):
    global cnt
    cnt += 1
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return recursion(s, l + 1, r - 1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

n = int(input())
for i in range(n):
    b = list(input().strip())
    cnt = 0
    result = isPalindrome(b)
    print(result, cnt)