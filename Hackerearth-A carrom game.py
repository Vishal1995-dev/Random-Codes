'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
n=int(input())
black=list(map(int,input().split()))
white=list(map(int,input().split()))
black.sort()
white.sort()
red=int(input())
p,q,r,s=map(int,input().split())
flag=0
i=1
win=0
while(flag==0):
    if(i==1):
        flag1=0
        if(len(black)==0):
            if(red<=p):
                win=1
                flag=1
            else:
                p+=1
                flag1=1
        for b in range(len(black)-1,-1,-1):
            if(p>=black[b]):
                p+=black[b]
                black.pop(b)
                flag1=1
                break
        if(flag1==0):
            p+=1
        i+=1
    elif(i==2):
        flag1=0
        if(len(white)==0):
            if(red<=q):
                win=2
                flag=1
            else:
                q+=1
                flag1=1
        for b in range(len(white)-1,-1,-1):
            if(q>=white[b]):
                q+=white[b]
                white.pop(b)
                flag1=1
                break
        if(flag1==0):
            q+=1
        i+=1
    elif(i==3):
        flag1=0
        if(len(black)==0):
            if(red<=r):
                win=1
                flag=1
            else:
                r+=1
                flag1=1
        for b in range(len(black)-1,-1,-1):
            if(r>=black[b]):
                r+=black[b]
                black.pop(b)
                flag1=1
                break
        if(flag1==0):
            r+=1
        i+=1
    elif(i==4):
        flag1=0
        if(len(white)==0):
            if(red<=s):
                win=2
                flag=1
            else:
                s+=1
                flag1=1
        for b in range(len(white)-1,-1,-1):
            if(s>=white[b]):
                s+=white[b]
                white.pop(b)
                flag1=1
                break
        if(flag1==0):
            s+=1
        i=1
if(win==1):
    print("A-C")
else:
    print("B-D")
