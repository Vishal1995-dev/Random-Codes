class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if(n==0):
            return 1
        i=1
        while(i-1<n):
            i*=2
        return i-n-1
