class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret=[0]*len(nums)
        i=0
        j=1
        for k in nums:
            if(k%2==0):
                ret[i]=k
                i+=2
            else:
                ret[j]=k
                j+=2
        return ret
