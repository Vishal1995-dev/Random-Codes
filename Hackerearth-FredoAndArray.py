'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
n=int(input())
a=list(map(int,input().split()))
i=0
s=sum(a)
while(i*n<=s):
    i+=1
print(i)
