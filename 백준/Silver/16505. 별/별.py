import sys
import math

def triangle(ans,n,m):
    if n==1:
        return '*'
    else:
        tmp=list(triangle(ans,n-1,m-1).split('\n'))
        for i in range(len(tmp)):
            ans+=tmp[i]*2
            ans+=' '*(2**m-len(tmp[i]*2))
            ans+='\n'

        for i in range(len(tmp)-1):
            ans+=tmp[i]
            ans += ' ' * (2 ** m - len(tmp[i]))
            ans+='\n'
        ans+=tmp[-1]
        ans+=' '*(2**m-len(tmp[-1]))
        return ans

if __name__=="__main__":
    n=int(input())
    ans=triangle('',n+1,n)
    for i in range(0,2**(n*2),(2**n+1)):
        ans1=ans[i:i+2**n]
        start=-1
        for s in range(len(ans1)-1,-1,-1):
            if ans1[s]=='*':
                start=s
                break
        for s in range(start+1):
            print(ans1[s],end='')
        print()