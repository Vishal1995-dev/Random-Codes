class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        i=0
        ret=0
        while(i<len(s)):
            cnt=0
            a=s[i]
            j=i
            flag=0
            while(j<len(s) and s[i]==s[j]):
                cnt+=1
                j+=1
                flag=1
            if(cnt>ret):
                ret=cnt
            if(flag==1):
                i=j
            else:
                i+=1
        return ret
