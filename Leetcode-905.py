class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s=0
        e=len(nums)-1
        while(s<e):
            if(nums[s]%2!=0 and nums[e]%2==0):
                nums[e],nums[s]=nums[s],nums[e]
                s+=1
                e-=1
            if(nums[s]%2==0):
                s+=1
            if(nums[e]%2!=0):
                e-=1     
        return nums
