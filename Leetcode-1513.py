class Solution(object):
    def numSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        a={}
        i=0
        while(i<len(s)):
            if(s[i]=='1'):
                cnt=0
                while(i<len(s) and s[i]=='1'):
                    cnt+=1
                    i+=1
                if(cnt in a):
                    a[cnt]+=1
                else:
                    a[cnt]=1
            i+=1
        ret=0
        for i in a:
            n=i*(i+1)//2
            ret+=(n*a[i])
        return ret%1000000007
