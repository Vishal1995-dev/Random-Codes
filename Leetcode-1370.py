class Solution(object):
    def sortString(self, s):
        """
        :type s: str
        :rtype: str
        """
        d={}
        a=[]
        for i in s:
            if(i in d):
                d[i]+=1
            else:
                a.append(i)
                d[i]=1
        a.sort()
        ret=""
        flag=0
        while(len(ret)!=len(s)):
            if(flag==0):
                for i in a:
                    if(d[i]!=0):
                        ret+=i
                        d[i]-=1
                flag=1
            else:
                for i in range(len(a)-1,-1,-1):
                    if(d[a[i]]!=0):
                        ret+=a[i]
                        d[a[i]]-=1
                flag=0
        return ret
