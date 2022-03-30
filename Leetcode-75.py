class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        d={}
        d[0]=0
        d[1]=0
        d[2]=0
        for i in nums:
            d[i]+=1
        p=0
        for i in d:
            while(d[i]!=0):
                nums[p]=i
                p+=1
                d[i]-=1  
        return nums
