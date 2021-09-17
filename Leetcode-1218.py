class Solution(object):
    def longestSubsequence(self, arr, difference):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """
        dp={}
        ret=1
        for i in range(len(arr)-1,-1,-1):
            if(arr[i]+difference in dp):
                dp[arr[i]]=dp[arr[i]+difference]+1
            else:
                dp[arr[i]]=1
            ret=max(dp[arr[i]],ret)
        return ret
