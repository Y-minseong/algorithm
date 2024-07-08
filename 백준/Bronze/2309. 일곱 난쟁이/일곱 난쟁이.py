s = []
for i in range(9):
    s.append(int(input()))
    
s.sort()

num = sum(s)

liar = []

for i in range(9):
    for j in range(i + 1, 9):
        if num - s[i] - s[j] == 100:
            liar.append(s[i])
            liar.append(s[j])
            break
    if len(liar) == 2:
        break
    
for i in s:
    if i not in liar:
        print(i)