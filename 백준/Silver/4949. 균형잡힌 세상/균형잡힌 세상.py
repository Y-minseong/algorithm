import sys
input = sys.stdin.read

def is_balanced(string):
    stack = []
    for char in string:
        if char in "([": 
            stack.append(char)
        elif char == ")":  
            if not stack or stack[-1] != "(":  
                return False
            stack.pop() 
        elif char == "]":  
            if not stack or stack[-1] != "[": 
                return False
            stack.pop()  
    return not stack 

def main():
    lines = input().splitlines()
    results = []
    for line in lines:
        if line == ".": 
            break
        results.append("yes" if is_balanced(line) else "no")
    print("\n".join(results))

if __name__ == "__main__":
    main()
