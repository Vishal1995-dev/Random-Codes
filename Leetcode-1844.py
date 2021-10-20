class Solution(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        ret=""
        for i in range(1,len(s),2):
            ret+=s[i-1]
            ret+=chr(ord(s[i-1])+ord(s[i])-ord('0'))
        if(len(s)%2!=0):
            ret+=s[len(s)-1]
        return ret
