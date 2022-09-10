class Solution(object):
    def findPoisonedDuration(self, t, d):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        ret=d
        for i in range(len(t)-1):
            if(t[i]+d>t[i+1]):
                ret+=t[i+1]-t[i]
            else:
                ret+=d
        return ret
    
