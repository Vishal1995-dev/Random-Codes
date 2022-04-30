class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=float('-inf')
        b=float('-inf')
        c=float('-inf')
        for i in nums:
            if(i>a):
                a,b,c=i,a,b
            elif(i>b and i!=a):
                c,b=b,i
            elif(i>c and i!=a and i!=b):
                c=i
        if(c==float('-inf')):
            return a
        return c
                
