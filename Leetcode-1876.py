class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret=0
        for i in range(0,len(s)-2):
            if(len(set(s[i:i+3]))==3):
                ret+=1
        return ret
