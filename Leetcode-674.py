class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret=0
        s=1
        for i in range(1,len(nums)):
            if(nums[i]>nums[i-1]):
                s+=1
            else:
                ret=max(ret,s)
                s=1
        ret=max(ret,s)
        return ret
