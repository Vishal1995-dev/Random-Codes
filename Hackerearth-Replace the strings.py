'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
t=int(input())
for _ in range(t):
    l=int(input())
    s=list(input())
    t=list(input())
    set_s=set(s)
    set_t=set(t)
    a={}
    a[1]=0
    a[-1]=0
    flag=0
    for i in set_s:
        if(abs(s.count(i)-t.count(i))>1):
            print("NO")
            flag=1
            break
        else:
            if(abs(s.count(i)-t.count(i))!=0):
                a[s.count(i)-t.count(i)]+=1
                if(a[s.count(i)-t.count(i)]>1):
                    print("NO")
                    flag=1
                    break
    if(flag==0):
        print("YES")
    
