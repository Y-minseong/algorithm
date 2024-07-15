import sys

def front(root): # 전위 순회 root > left > right
    if root != '.':
        print(root, end = '') # root
        front(node[root][0]) # left
        front(node[root][1]) # right
        return 

def middle(root): # 중위 순회 left > root > right
    if root != '.':
        middle(node[root][0]) # left
        print(root, end = '') # root
        middle(node[root][1]) # right

def back(root): # 후위 순회 left > right > root
    if root != '.':
        back(node[root][0]) # left
        back(node[root][1]) # right
        print(root, end = '') # root




num = int(input())
node = {}
for i in range(num):
    root, left, right = sys.stdin.readline().strip().split()
    node[root] = [left, right]

front("A")
print()
middle("A")
print()
back("A")