class Solution {
public:
    vector<vector<int>> shiftGrid(vector<vector<int>>& grid, int k) {
        vector<int> a;
        int n=grid.size();
        int m=grid[0].size();
        
        for(int i=0;i<n;i++) {
            for(int j=0;j<m;j++) a.push_back(grid[i][j]);
        }
        
        k=k%(n*m);
        
        for(int i=0;i<n;i++) {
            for(int j=0;j<m;j++) {
                if(k>0) grid[i][j]=a[(n*m)-k];
                else grid[i][j]=a[-k];
                k--;
            }
        }
        return grid;
    }
};
