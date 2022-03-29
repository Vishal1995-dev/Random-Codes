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
            if(r[i]-r[i-1]==ret and k[i]>val) or r[i]-r[i-1]>ret:
                ret=r[i]-r[i-1]
                val=k[i]
        return val
        
