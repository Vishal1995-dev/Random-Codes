class Solution(object):
    def canThreePartsEqualSum(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        s=sum(arr)
        if(s%3!=0):
            return False
        v=s//3
        ret=0
        su=0
        for i in arr:
            su+=i
            if(su==v):
                ret+=1
                su=0
        return ret>=3
