class Solution(object):
    def checkAlmostEquivalent(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        a=[0]*26
        b=[0]*26
        for i in range(len(word1)):
            a[ord(word1[i])-ord('a')]+=1
            b[ord(word2[i])-ord('a')]+=1
        for i in range(26):
            if(abs(a[i]-b[i])>3):
                return False
        return True
