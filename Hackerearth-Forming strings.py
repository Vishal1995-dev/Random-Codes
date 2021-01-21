def solve(n):
        i=1
        ret=5
        while(i<n):
                if(i%2==0):
                        ret=ret*2+1
                else:
                        ret=ret*2-1
                i+=1
        return ret%(10**9+7)

T = int(input())
for _ in range(T):
    N = int(input())
    out_ = solve(N)
    print (out_)
