class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        ret=start
        i=1
        while(i<n):
            ret^=start+2*i
            i+=1
        return ret
