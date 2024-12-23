N = int(input())
num = list(map(int, input().split()))
number = int(input())
n = 0

for i in range(len(num)):
    if num[i] == number:
        n += 1
print(n)