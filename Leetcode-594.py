class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=set(nums)
        ret=0
        for i in n:
            if((i+1) in n):
                no=nums.count(i)+nums.count(i+1)
                if(no>ret):
                    ret=no
        return ret
