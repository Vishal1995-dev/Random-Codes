class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m1=0
        m2=0
        i=0
        for k in range(len(nums)):
            if(nums[k]>=m1):
                m2=m1
                m1=nums[k]
                i=k
            elif(nums[k]>=m2):
                m2=nums[k]
        if(m1>=2*m2):
            return i
        return -1
