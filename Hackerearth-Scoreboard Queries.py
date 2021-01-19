'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
t=int(input())
for _ in range(t):
    n,q=map(int,input().split())
    s=list(map(int,input().split()))
    a={}
    for i in s:
        if(i in a):
                a[i]+=1
        else:
                a[i]=1
    for j in range(q):
        l,r=map(int,input().split())
        a[s[l-1]]-=1
        if(a[s[l-1]]==0):
                del a[s[l-1]]
        s[l-1]=r
        if(r in a):
                a[r]+=1
        else:
                a[r]=1
        print(len(a)+1)
