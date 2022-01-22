class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret=0
        nums.sort()
        for i in range(1,len(nums)):
            ret=max(ret,nums[i]-nums[i-1])
        return ret
