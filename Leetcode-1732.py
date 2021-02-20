class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        s=0
        ret=0
        for i in gain:
            s+=i
            ret=max(ret,s)
        return ret
