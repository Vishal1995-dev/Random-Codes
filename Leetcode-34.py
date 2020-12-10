class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ret=[-1,-1]
        i=0
        while(i<len(nums)):
            if(nums[i]==target):
                ret[0]=i
                ret[1]=i
                while(i<len(nums) and nums[i]==target):
                    i+=1
                ret[1]=i-1
                return ret
            i+=1
        return ret
