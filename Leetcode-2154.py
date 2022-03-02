class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        d={}
        for i in nums:
            d[i]=1
        while(original in d):
            original*=2
        return original
