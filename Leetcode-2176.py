class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l=len(nums)
        d={}
        for i in range(l):
            if(nums[i] in d):
                d[nums[i]].append(i)
            else:
                d[nums[i]]=[i]
        ret=0
        for i in d:
            l=len(d[i])
            for j in range(l):
                for m in range(j+1,l):
                    if((d[i][m]*d[i][j])%k==0):
                        ret+=1
        return ret
