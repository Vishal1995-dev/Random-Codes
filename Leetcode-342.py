class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if(n<1):
            return False
        if(n==1):
            return True
        i=1
        while(i<=n):
            i=i*4
            if(i==n):
                return True
        return False
