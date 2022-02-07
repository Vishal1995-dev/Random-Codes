class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        s=0
        p=1
        while(n!=0):
            val=n%10
            s+=val
            p*=val
            n//=10
        return p-s
