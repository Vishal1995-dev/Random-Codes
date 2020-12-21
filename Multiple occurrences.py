'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b={}
    for i in range(n):
        if(a[i] in b):
            b[a[i]].append(i)
        else:
            b[a[i]]=[i]
    ret=0
    for i in b:
        ret+=b[i][-1]-b[i][0]
    print(ret)
