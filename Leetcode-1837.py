class Solution(object):
    def sumBase(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        ret=0
        while(n):
            ret+=n%k
            n//=k
        return ret
