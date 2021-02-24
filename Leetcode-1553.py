class Solution(object):
    def minDays(self, m):
        """
        :type n: int
        :rtype: int
        """
        dp={}
        dp[0]=0
        dp[1]=1
        
        def eat(n):
            if(n in dp):
                return dp[n]
            dp[n]=1+min(n%2+eat(n//2),n%3+eat(n//3))
            return dp[n]
        
        ret=eat(m)
        return ret
