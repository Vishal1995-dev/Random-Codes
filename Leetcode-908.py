class Solution(object):
    def smallestRangeI(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        _max=max(nums)
        _min=min(nums)
        return max(_max-_min-2*k,0)
