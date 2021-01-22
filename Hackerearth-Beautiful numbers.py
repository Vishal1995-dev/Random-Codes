
import sys
import math

def divisor(i):
    s=math.sqrt(i)
    return ((s-math.floor(s))==0)

def Solve (N, A, K):
    # Write your code here
    B=[]
    for i in range(N):
        if(divisor(A[i])==True):
            B.append(i)
    ret=sys.maxsize
    if(len(B)<K):
        return -1
    if(len(B)==K):
        return B[-1]-B[0]+1
    for i in range(len(B)-K+1):
        if(B[i+K-1]-B[i]<ret):
            ret=B[i+K-1]-B[i]
    return ret+1
         

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    K = int(input())

    out_ = Solve(N, A, K)
    print (out_)
