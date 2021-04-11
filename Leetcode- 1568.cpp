class Solution {
public:
    int arr[4][2]={{0,1},{0,-1},{-1,0},{1,0}};
    void dfs(vector<vector<int>> &grid,vector<vector<int>> &visited,int i,int j,int n,int m)
    {
        visited[i][j]=1;
        for(int p=0;p<4;p++)
        {
            int new_i=i+arr[p][0];
            int new_j=j+arr[p][1];
            if(new_i<n && new_i>=0 && new_j<m && new_j>=0 && visited[new_i][new_j]==0 && grid[new_i][new_j]==1)
            {
                dfs(grid,visited,new_i,new_j,n,m);
            }
        }
    }
    
    int countIsland(vector<vector<int>>& grid,int n,int m)
    {
        vector<vector<int>> visited( n , vector<int> (m, 0));
        int count=0;
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                if(visited[i][j]==0 and grid[i][j]==1)
                {
                    dfs(grid,visited,i,j,n,m);
                    count+=1;
                }
            }
        }
        return count;
    }
    
    int minDays(vector<vector<int>>& grid) {    
        int n=grid.size();
        int m=grid[0].size();
        
        
        int count=countIsland(grid,n,m);
        
        if(count>1)
        {
            return 0;
        }
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                if(grid[i][j]==1)
                {
                    grid[i][j]=0;
                    count=countIsland(grid,n,m);
                    if(count!=1) return 1;
                    grid[i][j]=1;
                }
            }
        }
        return 2;
    }
};
