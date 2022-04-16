class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret1=0
        ret2=0
        for i in range(len(s)):
            if(i%2==0):
                if(s[i]=='1'):
                    ret1+=1
                if(s[i]=='0'):
                    ret2+=1
            else:
                if(s[i]=='0'):
                    ret1+=1
                if(s[i]=='1'):
                    ret2+=1
        return min(ret1,ret2)
