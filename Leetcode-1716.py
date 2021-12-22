class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret=0
        s=1
        while(n>=7):
            ret+=(7)*(s+3)
            n-=7
            s+=1
        ret+=(n*((2*s)+(n-1)))//2
        return ret
