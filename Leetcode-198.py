class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def robnew(i):
            if(i<0):
                return 0
            if(dp[i]!=0):
                return dp[i]
            dp[i]=max(robnew(i-1),nums[i]+robnew(i-2))
            return dp[i]
        dp=[0]*len(nums)
        return robnew(len(nums)-1)
    
