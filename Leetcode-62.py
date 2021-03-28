class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        self.ret=0
        
        def move(i,j):
            if(i>=m or j>=n):
                return
            if(i==m-1 and j==n-1):
                self.ret+=1
            move(i+1,j)
            move(i,j+1)
        
        move(0,0)
        return self.ret
        """
        dp=[]
        for i in range(m):
            d=[]
            for j in range(n):
                if(i==m-1 or j==n-1):
                    d.append(1)
                else:
                    d.append(0)
            dp.append(d)
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                dp[i][j]=dp[i+1][j]+dp[i][j+1]
        return dp[0][0]
