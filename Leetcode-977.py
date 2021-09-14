class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        ret=[0]*(n)
        i=0
        j=n-1
        for p in range(n-1,-1,-1):
            if(abs(nums[i])>abs(nums[j])):
                ret[p]=nums[i]*nums[i]
                i+=1
            else:
                ret[p]=nums[j]*nums[j]
                j-=1
        return ret
