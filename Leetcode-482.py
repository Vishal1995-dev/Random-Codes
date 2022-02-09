class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        ret=""
        s=s.upper()
        i=len(s)-1
        j=0
        while(i>=0):
            if(s[i]!='-'):
                ret+=s[i]
                j+=1
            i-=1
            if(j==k):
                j=0
                ret+="-"
        if(len(ret)==0):
            return ret
        if(ret[-1]=='-'):
            return ret[:-1][::-1]
        else:
            return ret[::-1]
