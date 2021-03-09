class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if(len(s)==1):
            return False
        l=set(list(s))
        n1=s.count(s[0])
        for i in l:
            if(s.count(i)!=n1):
                return False
        n=len(s)
        for i in range(n//2+1):
            if(s.count(s[:i])*i==n):
                return True
        return False
