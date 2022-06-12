class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=b=999999999
        c=d=-1
        for i in nums:
            if(i<a):
                b=a
                a=i
            elif(i<b):
                b=i
            if(i>d):
                c=d
                d=i
            elif(i>c):
                c=i
        return d*c-a*b
    
