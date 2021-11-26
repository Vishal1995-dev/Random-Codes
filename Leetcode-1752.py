class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a=[nums[0]]
        i=1
        while(i<len(nums) and nums[i]>=nums[i-1]):
            a.append(nums[i])
            i+=1
        if(i==len(nums)):
            return True
        b=[nums[i]]
        i+=1
        while(i<len(nums) and nums[i]>=nums[i-1]):
            b.append(nums[i])
            i+=1
        nums.sort()
        return b+a==nums
