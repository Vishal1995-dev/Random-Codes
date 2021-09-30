class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        dp=[0]*n
        dp[0]=nums[0]
        ret=dp[0]
        for i in range(1,n):
            dp[i]=nums[i]+max(dp[i-1],0)
            ret=max(ret,dp[i])
        return ret
