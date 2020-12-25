class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret=0
        nums.sort()
        for i in range(0,len(nums),2):
            ret+=nums[i]
        return ret
