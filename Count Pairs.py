def gcd(x,y):
    while(y):
        x,y=y,x%y
    return x

def solve (N, G, A):
    # Type your code here
    ret=[]
    for i in range(N):
        cnt=0
        if(A[i]%G!=0):
            ret.append(0)
            continue
        for j in range(i+1,N):
            if(A[j]%G!=0):
                continue
            if((A[i]%A[j]==0 or A[j]%A[i]==0) and (A[i]!=G and A[j]!=G)):
                continue
            if(gcd(A[i],A[j])==G):
                cnt+=1
        ret.append(cnt)
    return ret

T = input()
for _ in xrange(T):
    N, G = map(int, raw_input().split())
    A = map(int, raw_input().split())

    out_ = solve(N, G, A)
    print ' '.join(map(str, out_))
