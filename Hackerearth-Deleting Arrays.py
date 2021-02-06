'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    if(n%(2*k+1)==0):
        print(n//(2*k+1))
    else:
        print(n//(2*k+1)+1)
