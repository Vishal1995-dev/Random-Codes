class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        i=0
        j=1
        while(k>0):
            if(i<len(arr) and arr[i]==j):
                i+=1
                j+=1
            else:
                k-=1
                j+=1
        return(j-1)
