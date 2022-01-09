class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d={}
        cnt=0
        for i in s:
            if(i in d):
                d[i]+=1
            else:
                d[i]=1
            cnt=d[i]
        for i in d:
            if(d[i]!=cnt):
                return False
        return True
