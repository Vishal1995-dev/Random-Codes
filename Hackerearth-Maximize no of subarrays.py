def solve (n, k, arr):
    # Write your code here
    ret=0
    odd=0
    i=0
    while(i<(n-1)):
        if(arr[i]%2==0):
            ret+=1
            i+=1
        else:
            if(arr[i+1]%2==0):
                odd+=1
                ret+=1
                i+=2
            else:
                ret+=1
                i+=2
    
    if(i<n):
        if(arr[i]%2==0):
            ret+=1
        else:
            odd+=1

    
    while(k>0 and odd>1):
        ret+=1
        odd-=2
        k-=1
    return ret
    
T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    out_ = solve(n, k, arr)
    print (out_)
