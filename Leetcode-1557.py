class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        ret=[]
        d=[0]*n
        for i in edges:
            d[i[1]]=1
        for i in range(n):
            if(d[i]==0):
                ret.append(i)
        return ret
