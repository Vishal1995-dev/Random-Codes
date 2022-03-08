class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ret=99999999
        nums.sort()
        for i in range(k-1,len(nums)):
            ret=min(ret,nums[i]-nums[i-k+1])
        return ret
