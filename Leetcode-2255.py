class Solution(object):
    def countPrefixes(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: int
        """
        ret=0
        l=len(s)
        for i in words:
            if(len(i)<=l):
                if(s[:len(i)]==i):
                    ret+=1
        return ret
