def plus(n):
    a = n
    count = 0
    
    while True:
        if n < 10:
            n = '0{0}'.format(n)
        else:
            n = str(n)
            
        n0 = n[-1]
        n1 = str(int(n[0]) + int(n[1]))[-1]
        
        new = int(n0 + n1)
        count += 1
        
        if new == a:
            break
        n = new

    return count

num = int(input())
print(plus(num))

