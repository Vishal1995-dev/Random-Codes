class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        ret=0
        visited=[]
        for i in range(len(grid)):
            a=[]
            for j in range(len(grid[0])):
                a.append(0)
            visited.append(a)
        
        def dfs(n,m):
            if(n>=len(grid) or n<0 or m>=len(grid[0]) or m<0):
                return  
            visited[n][m]=1
            if(m+1<len(grid[0]) and grid[n][m+1]=='1' and visited[n][m+1]==0):
                dfs(n,m+1)
            if(m-1>=0 and grid[n][m-1]=='1' and visited[n][m-1]==0):
                dfs(n,m-1)
            if(n+1<len(grid) and grid[n+1][m]=='1' and visited[n+1][m]==0):
                dfs(n+1,m)
            if(n-1>=0 and grid[n-1][m]=='1' and visited[n-1][m]==0):
                dfs(n-1,m)
            return
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]=='1' and visited[i][j]==0):
                    dfs(i,j)
                    ret+=1
        return ret
