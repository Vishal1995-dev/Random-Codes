class Solution(object):
    def kidsWithCandies(self, candies, e):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        m=max(candies)
        ret=[]
        for i in candies:
            if(i+e>=m):
                ret.append(True)
            else:
                ret.append(False)
        return ret
