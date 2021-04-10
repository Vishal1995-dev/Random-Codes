class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        while(nums):
            a=nums[0]
            i=1
            while(a in nums):
                if(a+1 in nums and nums.count(a)>nums.count(a+1)):
                    nums.remove(a)
                    i+=1
                    break
                nums.remove(a)
                a+=1
                i+=1
            if(i<=3):
                return False
        return True
