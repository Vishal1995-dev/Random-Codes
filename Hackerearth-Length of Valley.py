t=int(input())
for _ in range(t):
   n=int(input())
   ret=[1]*n
   a=list(map(int,input().split()))
   for i in range(1,n):
       if(a[i]<a[i-1]):
           ret[i]+=ret[i-1]
   ret2=[1]*n
   for i in range(n-2,-1,-1):
       if(a[i+1]>a[i]):
           ret2[i]+=ret2[i+1]
   for i in range(n):
       print(ret[i]+ret2[i]-1,end=" ")
   print()
