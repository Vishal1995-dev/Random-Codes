class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        ret=0
        for i in sorted(boxTypes,key=lambda x:x[1],reverse=True):
            if(i[0]<truckSize):
                ret+=(i[0]*i[1])
                truckSize-=i[0]
            else:
                ret+=i[1]*truckSize
                break
        return ret
