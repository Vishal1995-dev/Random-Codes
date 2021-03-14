class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        c=[]
        r=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if(matrix[i][j]==0):
                    r.append(i)
                    c.append(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if(i in r or j in c):
                    matrix[i][j]=0
        return
