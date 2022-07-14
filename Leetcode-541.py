class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        ret=""
        l=len(s)
        i=0
        while(i<l):
            if(i+k<=l):
                ret+=s[i:i+k][::-1]
                i+=k
            else:
                ret+=s[i:l][::-1]
                break
            if(i+k<=l):
                ret+=s[i:i+k]
                i+=k
            else:
                ret+=s[i:l]
                break
        return ret
