class Solution {
public:
    int calculateMinimumHP(vector<vector<int>>& dungeon) {
        int m=dungeon.size();
        int n=dungeon[0].size();
        
        vector<vector<int> > h(m + 1, vector<int>(n + 1, INT_MAX));
        h[m-1][n]=1;
        h[m][n-1]=1;
        
        for(int i=m-1;i>=0;i--) {
            for(int j=n-1;j>=0;j--) {
                h[i][j]=max(min(h[i+1][j],h[i][j+1])-dungeon[i][j],1);
            }
        }
        
        return h[0][0];
    }
};
