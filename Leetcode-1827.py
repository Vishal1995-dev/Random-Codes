class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j=1
        ret=0
        while(j<len(nums)):
            if(nums[j]<=nums[j-1]):
                ret+=(nums[j-1]-nums[j]+1)
                nums[j]=nums[j-1]+1
            j+=1
        return ret
