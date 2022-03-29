class Solution(object):
    def slowestKey(self, r, k):
        """
        :type releaseTimes: List[int]
        :type keysPressed: str
        :rtype: str
        """
        ret=r[0]
        val=k[0]
        for i in range(1,len(r)):
            if(r[i]-r[i-1]>=ret):
                if(k[i]>val or ret<r[i]-r[i-1]):
                    val=k[i]
                ret=r[i]-r[i-1]
        return val
        
