class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ret=0
        def getData(n,m):
            if(n>=0 and m>=0 and n<len(grid) and m<len(grid[0])):
                return grid[n][m]
            return 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]==1):
                    if(getData(i-1,j)==0):
                        ret+=1
                    if(getData(i,j-1)==0):
                        ret+=1
                    if(getData(i+1,j)==0):
                        ret+=1
                    if(getData(i,j+1)==0):
                        ret+=1
        return ret
