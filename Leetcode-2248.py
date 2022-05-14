class Solution(object):
    def intersection(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        ret=[]
        d={}
        l=len(nums)
        for i in nums:
            for j in i:
                if(j in d):
                    d[j]+=1
                else:
                    d[j]=1
                if(d[j]==l):
                    ret.append(j)
        ret.sort()
        return ret
