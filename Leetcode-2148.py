class Solution(object):
    def countElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        s=nums[0]
        e=nums[-1]
        i=0
        j=len(nums)-1
        while(i<=j and nums[i]==s):
            i+=1
        while(j>=i and nums[j]==e):
            j-=1
        return j-i+1
