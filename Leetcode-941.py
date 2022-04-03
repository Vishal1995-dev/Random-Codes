class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        l=len(arr)
        i=0
        while(i+1<l and arr[i]<arr[i+1]):
            i+=1
        if(i==0 or i==l-1):
            return False
        while(i+1<l and arr[i]>arr[i+1]):
            i+=1
        return i==l-1
