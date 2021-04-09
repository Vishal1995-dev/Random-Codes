s=input()
a=[0]*len(s)

if(int(s[len(s)-1])%2==0):
    a[len(s)-1]=1
else:
    a[len(s)-1]==0

for i in range(2,len(s)):
	a[len(s)-i]=a[len(s)-i+1]+(1-int(s[len(s)-i])%2)
a[0]=a[1]+(1-int(s[0])%2)

for i in a:
    print(i,end=' ')
