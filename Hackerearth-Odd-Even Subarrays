ret=0
difference=0
n=int(input())
a=list(map(int,input().split()))
hash_positive=[0]*(n+1)
hash_negative=[0]*(n+1)
hash_positive[0]=1
for i in a:
    if(i%2==0):
        difference+=1
    else:
        difference-=1

    if(difference<0):
        ret+=hash_negative[-difference]
        hash_negative[-difference]+=1
    else:
        ret+=hash_positive[difference]
        hash_positive[difference]+=1
print(ret)
