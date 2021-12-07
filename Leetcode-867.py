class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        n=len(matrix)
        m=len(matrix[0])
        ret=[[None] * n for _ in xrange(m)]
        for i in range(n):
            for j in range(m):
                ret[j][i]=matrix[i][j]
        return ret
