class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums)==0):
            return 0
        nums=map(int,nums)
        nums=list(set(nums))
        nums.sort()
        ret=1
        j=nums[0]
        i=1
        while(i<len(nums)):
            s=1
            if(nums[i]==j+1):
                while(i<len(nums) and nums[i]==j+1):
                    s+=1
                    j=nums[i]
                    i+=1
            else:
                j=nums[i]
                i+=1
            ret=max(ret,s)
        return ret
