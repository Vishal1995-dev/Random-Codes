class Solution(object):
    def checkString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i=0
        for i in range(len(s)):
            if(s[i]=='b'):
                break
        if(i==len(s)-1 and s[i]!='b'):
            return True
        j=len(s)-1
        for j in range(len(s)-1,-1,-1):
            if(s[j]=='a'):
                break
        if(j==0 and s[j]!='a'):
            return True
        return i>j
