n=int(input())
a=list(map(int,input().split()))
a.sort()
q=int(input())
for i in range(q):
    p=int(input())
    s=0
    e=len(a)-1
    while(s<e):
        mid=int((s+e)/2)
        if(a[s]==p):
            print(s+1)
            break
        elif(a[e]==p):
            print(e+1)
            break
        elif(a[mid]==p):
            print(mid+1)
            break
        else:
            if(p>a[mid]):
                s=mid+1
            else:
                e=mid-1
