class Solution(object):
    def generate(self, n):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ret=[[1]]
        for i in range(1,n+1):
            a=[0]*i
            a[0]=1
            a[-1]=1
            for j in range(1,i-1):
                a[j]=ret[i-1][j-1]+ret[i-1][j]
            ret.append(a)
        ret.pop(0)
        return ret
