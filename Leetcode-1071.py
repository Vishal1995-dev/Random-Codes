class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        i=n=len(str1)
        l=len(str2)
        while(i>0):
            c1=str1.count(str1[:i])
            if(c1*(i)==n):
                c1=str2.count(str1[:i])
                if(c1*(i)==l):
                    return str1[:i]
            i-=1
            
        return ""
