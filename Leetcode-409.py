class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        d={}
        cnt=0
        for i in s:
            if(i in d):
                if(d[i]==1):
                    d[i]=0
                    cnt+=2
                else:
                    d[i]=1
            else:
                d[i]=1
        for i in s:
            if(d[i]==1):
                cnt+=1
                break
        return cnt
