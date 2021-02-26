t=int(input())
for _ in range(t):
    n=int(input())
    a=[]*n
    row=0
    col=0
    trace=0
    for i in range(n):
        inp=list(map(int,input().split()))
        a.append(inp)
        s=set(inp)
        if(len(s)!=len(inp)):
            row+=1
    for i in range(n):
        p=[]
        for j in range(n):
            if(a[j][i] in p):
                col+=1
                break
            p.append(a[j][i])
    for i in range(n):
        trace+=a[i][i]
        
    print(f'Case #{(_+1)}:',trace,row,col)
