'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
t=int(input())
for _ in range (t):
    n=int(input())
    a=list(map(int,input().split()))
    e=0
    o=0
    for i in a:
        if(i%2==0):
            e+=1
        else:
            o+=1
    print(min(o,e))
