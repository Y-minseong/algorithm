n = int(input()) 
members = []

for _ in range(n):
    age, name = input().split()
    members.append((int(age), name)) 

members.sort(key=lambda member: member[0])

for age, name in members:
    print(age, name)
