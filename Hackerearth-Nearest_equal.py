def solve (n, A):
    # Write your code here
    ret=[]
    a={}
    for i in range(n):
        if(A[i] in a):
            a[A[i]].append(i)
        else:
            a[A[i]]=[i]
    for i in range(n):
        if(len(a[A[i]])==1):
            ret.append(-1)
        else:
            m=a[A[i]].index(i)
            if(m==0):
                ret.append(a[A[i]][1]-a[A[i]][0])
            elif(m==len(a[A[i]])-1):
                ret.append(a[A[i]][len(a[A[i]])-1]-a[A[i]][len(a[A[i]])-2])
            else:
                ret.append(min(a[A[i]][m]-a[A[i]][m-1],a[A[i]][m+1]-a[A[i]][m]))
    return ret

n = input()
A = map(int, raw_input().split())

out_ = solve(n, A)
print ' '.join(map(str, out_))
