class Solution(object):
    def sortEvenOdd(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret=[]
        a=[[],[]]
        for i in range(len(nums)):
            a[i%2].append(nums[i])
        a[0].sort()
        a[1].sort(reverse=True)
        for i in range(len(nums)):
            ret.append(a[i%2].pop(0))
        return ret
