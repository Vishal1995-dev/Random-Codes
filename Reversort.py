t=int(input())
for z in range(1,t+1):
    n=int(input())
    a=list(map(int,input().split()))
    ret=0
    for i in range(n-1):
        j=a.index(min(a[i:]))
        ret+=j-i+1
        a[i:j+1]=a[i:j+1][::-1]
    print(f'Case #{z}: {ret}')
