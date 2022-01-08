class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        def check(st):
            for i in st:
                if(i.islower() and chr(ord(i)-32) not in st):
                    return False
                if(i.isupper() and chr(ord(i)+32) not in st):
                    return False
            return True
            
        ret=""
        for i in range(len(s)):
            for j in range(i,len(s)):
                if(j+1-i>len(ret) and check(s[i:j+1])):
                    if(len(ret)<j+1-i):
                        ret=s[i:j+1]
        return ret
