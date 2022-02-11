class Solution(object):
    def checkValid(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        n=len(matrix)
        for i in matrix:
            if(len(i)!=len(set(i))):
                return False
        
        for i in range(n):
            v=set()
            for j in range(n):
                v.add(matrix[j][i])
            if(len(v)!=n):
                return False
        
        return True
