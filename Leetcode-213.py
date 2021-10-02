class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def rob(l,r):
            last=0
            curr=0
            for i in range(l,r+1):
                temp=max(last+nums[i],curr)
                last=curr
                curr=temp
            return curr
        
        if(len(nums)==1):
            return nums[0]
        return max(rob(1,len(nums)-1),rob(0,len(nums)-2))
