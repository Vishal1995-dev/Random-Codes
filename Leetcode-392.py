class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i=len(s)-1
        j=len(t)-1
        while(i!=-1):
            while(j>=0 and t[j]!=s[i]):
                j-=1
            if(j==-1):
                return False
            i-=1
            j-=1
        if(i!=-1):
            return False
        return True
