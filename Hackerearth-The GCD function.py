
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
    s=0
    l=[]
    for i in range(1,n+1):
        s+=i
        l.append(i)

    def find_lcm(num1, num2): 
        if(num1>num2): 
            num = num1 
            den = num2 
        else: 
            num = num2 
            den = num1 
        rem = num % den 
        while(rem != 0): 
            num = den 
            den = rem 
            rem = num % den 
        gcd = den 
        lcm = int(int(num1 * num2)/int(gcd)) 
        return lcm 

    if(len(l)==1):
        lcm=l[0]
    else:
        num1 = l[0] 
        num2 = l[1] 
        lcm = find_lcm(num1, num2) 

        for i in range(2, len(l)): 
            lcm = find_lcm(lcm, l[i]) 
    print(str(s)+" "+str(lcm)) 
