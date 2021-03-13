'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
t=int(input())
s1=input()
s2=input()
i=0
ret=0
while(i<t):
    if(s1[i]!=s2[i]):
        while(i<t and s1[i]!=s2[i]):
            i+=1
        ret+=1
    i+=1
print(ret)
