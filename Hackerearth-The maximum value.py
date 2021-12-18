'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
t=int(input())
for _ in range(t):
    a=int(input())
    dp=[0]*(a+1)
    i=2
    cnt=0
    while(i<=a):
        j=1
        while(i*j<=a):
            dp[i*j]=i
            j+=1
        cnt+=1
        while(i<=a and dp[i]!=0):
            i+=1
    print(cnt)
