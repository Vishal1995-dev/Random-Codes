class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ret=[]
        nums.sort()
        for i in range(len(nums)):
            if(nums[i]==target):
                ret.append(i)
            if(nums[i]>target):
                break
        return ret
