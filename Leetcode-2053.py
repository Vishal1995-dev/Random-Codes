class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        d={}
        for i in arr:
            if(i in d):
                d[i]+=1
            else:
                d[i]=1
        ret=""
        for i in arr:
            if(d[i]==1):
                k-=1
                d[i]=0
                if(k==0):
                    return i
        return ret
