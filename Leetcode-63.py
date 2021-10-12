class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        n=len(obstacleGrid)
        m=len(obstacleGrid[0])
        
        dp=[]
        for i in range(n):
            a=[]
            for j in range(m):
                a.append(0)
            dp.append(a)
        for i in range(m):
            if(obstacleGrid[0][i]!=1):
                dp[0][i]=1
            else:
                break
        for i in range(n):
            if(obstacleGrid[i][0]!=1):
                dp[i][0]=1
            else:
                break
        for i in range(1,n):
            for j in range(1,m):
                if(obstacleGrid[i][j]!=1):
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[n-1][m-1]
