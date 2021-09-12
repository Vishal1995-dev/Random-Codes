class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        a=[0]*60
        for i in time:
            a[i%60]+=1
        ret=0
        if(a[30]>0):
            ret=a[30]*(a[30]-1)/2
        if(a[0]>0):
            ret+=a[0]*(a[0]-1)/2
        for i in range(1,30):
            ret+=a[30-i]*a[30+i]
        return ret
