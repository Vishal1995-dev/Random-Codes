class Solution(object):
    def numOfStrings(self, patterns, word):
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
        ret=0
        for i in patterns:
            if(i in word):
                ret+=1
        return ret
