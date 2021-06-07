class Solution {
public:
    int ret=0;
    int dir[5] = {0, 1, 0, -1, 0};
    
    void traverse(int i,int j,int s,vector<vector<int>>& grid,int m,int n) {
        if(s>ret) ret=s;
        if(i<0 || j<0 || i>=m || j>=n || grid[i][j]==0) return;
        int val=grid[i][j];
        grid[i][j]=0;
        for(int q=0;q<4;q++) {
            traverse(i+dir[q],j+dir[q+1],s+val,grid,m,n);
        }
        grid[i][j]=val;
        }
    
    int getMaximumGold(vector<vector<int>>& grid) {
        int m=grid.size();
        int n=grid[0].size();
        for(int i=0;i<m;i++) {
            for(int j=0;j<n;j++) {
                if(grid[i][j]!=0) {
                    traverse(i,j,0,grid,m,n);
                }
            }
        }
        return ret;
    }
};
