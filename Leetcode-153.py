class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums)==1):
            return nums[0]
        low=0
        high=len(nums)-1
        if(nums[low]<nums[high]):
            return nums[low]
        while(low<=high):
            mid=(low+high)/2
            if(nums[mid]<nums[mid-1]):
                return nums[mid]
            if(nums[mid]>nums[mid+1]):
                return nums[mid+1]
            if(nums[mid]>nums[0]):
                low=mid+1
            else:
                high=mid-1
        
