class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret=0
        l=len(nums)
        m=nums[0]
        for i in range(l):
            if(nums[i]>m):
                ret=max(ret,nums[i]-m)
            m=min(m,nums[i])
        if(ret==0):
            return -1
        return ret
