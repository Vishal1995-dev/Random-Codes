class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ret=[0]*(n+1)
        offset=1
        for i in range(1,n+1):
            if(offset*2==i):
                offset*=2
            ret[i]=ret[i-offset]+1
        return ret
