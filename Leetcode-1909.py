class Solution(object):
    def canBeIncreasing(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l=len(nums)
        for i in range(l):
            li=nums[:i]+nums[i+1:]
            flag=0
            for j in range(1,l-1):
                if(li[j]<=li[j-1]):
                    flag=1
                    break
            if(flag==0):
                return True
        return False
