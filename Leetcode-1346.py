class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if(arr.count(0)>1):
            return True
        d={}
        for i in arr:
            if(i!=0):
                d[i]=1
        for i in arr:
            if(i*2 in d):
                return True
        return False
