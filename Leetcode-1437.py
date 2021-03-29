class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        a=0
        while(a<len(nums) and nums[a]!=1):
            a+=1
        for i in range(a+1,len(nums)):
            if(nums[i]==1):
                if(i-a<=k):
                    return False
                a=i
        return True
