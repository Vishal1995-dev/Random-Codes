class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        c={}
        for i in arr:
            if(i in c):
                c[i]+=1
            else:
                c[i]=1
        ret=-1
        for i in c:
            if(c[i]==i and i>ret):
                ret=i
        return ret
