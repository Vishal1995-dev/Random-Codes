class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        ret=0
        l=len(pref)
        for i in words:
            if(i[:l]==pref):
                ret+=1
        return ret
