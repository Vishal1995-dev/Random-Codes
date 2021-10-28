class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        n=len(arr)
        l=list(arr)
        l.sort(reverse=True)
        ret=[]
        for i in l:
            ind=arr.index(i)
            ret.append(ind+1)
            arr[:ind+1]=arr[:ind+1][::-1]
            ret.append(n)
            arr[:n]=arr[:n][::-1]
            n-=1
        return ret
