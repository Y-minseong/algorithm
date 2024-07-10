t = int(input())

height = list(map(int, input().split()))

stack = []

result = [0] * t

for i in range(t): # 5
    while len(stack):
        if height[stack[-1]] < height[i]:
         stack.pop()
        else:
         result[i] = stack[-1] + 1
         break
    stack.append(i)

print(*result)