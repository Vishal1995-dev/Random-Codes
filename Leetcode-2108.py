class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        def check(s):
            i=0
            j=len(s)-1
            while(i<j):
                if(s[i]!=s[j]):
                    return False
                i+=1
                j-=1
            return True
        
        for i in words:
            if(check(i)):
                return i
        return ""
