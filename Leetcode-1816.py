class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        a=s.split(" ")
        ret=a[:k]
        return " ".join(ret)
