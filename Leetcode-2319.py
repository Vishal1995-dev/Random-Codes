class Solution(object):
    def checkXMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        r=len(grid)
        c=len(grid[0])
        for i in range(r):
            for j in range(c):
                if(i==j or i+j==r-1):
                    if(grid[i][j]==0):
                        return False
                else:
                    if(grid[i][j]!=0):
                        return False
        return True
