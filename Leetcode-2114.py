class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        ret=0
        for i in sentences:
            ret=max(ret,i.count(" "))
        return ret+1
