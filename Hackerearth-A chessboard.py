
'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
t=int(input())
for _ in range(t):
    x1,y1=map(int,input().split())
    x2,y2=map(int,input().split())
    if(x2==x1 and y2==y1):
        print("SECOND")
    else:
        flag=0
        p=[[0,1],[0,-1],[-1,0],[1,0],[1,1],[-1,-1],[-1,1],[1,-1]]
        for i in p:
            x_new=x1+i[0]
            y_new=y1+i[1]
            if(x2==x_new and y2==y_new):
                flag=1
                print("FIRST")
                break
        if(flag==0):
            print("DRAW")
