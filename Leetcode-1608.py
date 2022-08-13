class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=len(nums)
        nums.sort()
        for i in range(0,nums[-1]+1):
            j=0
            while(nums[j]<i):
                j+=1
            if(l-j==i):
                return i
        return -1
