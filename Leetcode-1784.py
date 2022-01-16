class Solution(object):
    def checkOnesSegment(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i=0
        l=len(s)
        while(i<l):
            if(s[i]=='1'):
                while(i<l and s[i]=='1'):
                    i+=1
                break
            else:
                i+=1
        if(i==l):
            return True
        while(i<l):
            if(s[i]=='1'):
                return False
            i+=1
        return True
