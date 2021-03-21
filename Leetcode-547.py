class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        
        n=len(isConnected)
        visited=[0]*n
            
        def dfs(i):
            for q in range(n):
                if(visited[q]==0 and isConnected[i][q]==1):
                    visited[q]=1
                    dfs(q)
            return 
        s=0
        for i in range(n):
            if(visited[i]==0):
                s+=1
                dfs(i)
        return s
        
        
        
