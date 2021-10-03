class Solution(object):
    def maxScoreSightseeingPair(self, A):
        """
        :type values: List[int]
        :rtype: int
        """
        cur = res = 0
        for a in A:
            res = max(res, cur + a)
            cur = max(cur, a) - 1
            print(a,res,cur)
        return res
