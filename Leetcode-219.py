class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d={}
        for i in range(len(nums)):
            if(nums[i] in d):
                d[nums[i]].append(i)
            else:
                d[nums[i]]=[i]
        for i in d:
            if(len(d[i])>=2):
                for j in range(1,len(d[i])):
                    if(d[i][j]-d[i][j-1]<=k):
                        return True
        return False
