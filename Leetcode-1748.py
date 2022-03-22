class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret=0
        d={}
        for i in nums:
            if(i in d):
                d[i]+=1
            else:
                d[i]=1
        for i in d:
            if(d[i]==1):
                ret+=i
        return ret
