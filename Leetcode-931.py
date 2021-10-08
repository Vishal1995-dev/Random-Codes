class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        n=len(matrix)
        dp=[]
        for i in range(n):
            a=[]
            for j in range(n):
                a.append(0)
            dp.append(a)
        
        for i in range(n):
            dp[n-1][i]=matrix[n-1][i]
            
        for i in range(n-2,-1,-1):
            for j in range(n):
                if(j==0):
                    dp[i][0]=matrix[i][0]+min(dp[i+1][0],dp[i+1][1])
                elif(j==n-1):
                    dp[i][n-1]=matrix[i][n-1]+min(dp[i+1][n-1],dp[i+1][n-2])
                else:
                    dp[i][j]=matrix[i][j]+min(dp[i+1][j],dp[i+1][j-1],dp[i+1][j+1])
        return min(dp[0])
        
