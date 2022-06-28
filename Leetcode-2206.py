class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if(len(nums)%2==1):
            return False
        d={}
        for i in nums:
            if(i in d):
                d[i]+=1
            else:
                d[i]=1
        for i in d:
            if(d[i]%2!=0):
                return False
        return True
