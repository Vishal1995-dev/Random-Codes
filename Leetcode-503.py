class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=len(nums)
        ret=[-1]*l
        stack=[]
        for i in range(2*l-1,-1,-1):
            while(stack and nums[stack[-1]]<=nums[i%l]):
                stack.pop()
            if(stack):
                ret[i%l]=nums[stack[-1]]
            else:
                ret[i%l]=-1
            stack.append(i%l)
        return ret
