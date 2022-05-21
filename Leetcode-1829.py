class Solution(object):
    def getMaximumXor(self, nums, maximumBit):
        """
        :type nums: List[int]
        :type maximumBit: int
        :rtype: List[int]
        """
        ret=[]
        s=0
        for i in range(len(nums)):
            s=s^nums[i]
            nums[i]=s
        m=2**maximumBit-1
        for i in nums:
            ret.append(i^m)
        return ret[::-1]
