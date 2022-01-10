class Solution(object):
    def canFormArray(self, arr, pieces):
        """
        :type arr: List[int]
        :type pieces: List[List[int]]
        :rtype: bool
        """
        d={}
        for i in pieces:
            d[i[0]]=i
        ret=[]
        for i in arr:
            if(i in d):
                ret+=d[i]
        return ret==arr
