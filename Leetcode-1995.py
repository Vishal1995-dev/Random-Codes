class Solution(object):
    def countQuadruplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=len(nums)
        ret=0
        for i in range(l):
            for j in range(i+1,l):
                for k in range(j+1,l):
                    for m in range(k+1,l):
                        if(nums[i]+nums[j]+nums[k]==nums[m]):
                            ret+=1
        return ret
