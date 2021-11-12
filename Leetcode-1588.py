class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        ret=0
        n=len(arr)
        for i in range(n):
            for j in range(i,n,2):
                ret+=sum(arr[i:j+1])
        return ret
        
