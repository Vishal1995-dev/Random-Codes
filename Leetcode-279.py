class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[99999]*(n+1)
        i=1
        sq=[]
        while(i*i<=n):
            sq.append(i*i)
            dp[i*i]=1
            i+=1
        for i in range(1,n+1):
            for j in sq:
                if(i-j>0):
                    dp[i]=min(dp[i],1+dp[i-j])
                else:
                    break
        return dp[n]
