class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[0]*(n+1)
        dp[0]=0
        dp[1]=1
        for i in range(n+1):
            for j in range(1,i):
                dp[i]=max(dp[i],(i-j)*j,(i-j)*dp[j])
        return dp[n]
