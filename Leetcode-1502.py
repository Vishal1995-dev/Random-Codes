class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if(len(arr)<3):
            return True
        arr.sort()
        for i in range(1,len(arr)-1):
            if(arr[i+1]-arr[i]!=arr[i]-arr[i-1]):
                return False
        return True
        
