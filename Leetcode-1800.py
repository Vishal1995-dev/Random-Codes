class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        ret=0
        while(i<len(nums)):
            s=nums[i]
            while(i+1<len(nums) and nums[i]<nums[i+1]):
                s+=nums[i+1]
                i+=1
            ret=max(s,ret)
            i+=1
        return ret
