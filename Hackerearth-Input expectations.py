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
ret=0
j=0
while(i<n):
    if(a[i]+i>=n):
        ret+=a[i]+i-n+1
    i+=a[i]+1
    j+=1
ret+=n-j
print(ret)
    
