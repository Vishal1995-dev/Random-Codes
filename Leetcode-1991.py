class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=sum(nums)
        v=0
        for i in range(len(nums)):
            if(v==s-v-nums[i]):
                return i
            v+=nums[i]
        return -1
