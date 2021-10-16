class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp=[0]*(amount+1)
        dp[0]=1
        for j in coins:
            for i in range(j,amount+1):
                dp[i]+=dp[i-j]
        return dp[amount]
