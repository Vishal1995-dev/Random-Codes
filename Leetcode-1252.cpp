class Solution {
public:
    int oddCells(int m, int n, vector<vector<int>>& indices) {
        map<int,int> row;
        map<int,int> col;
        
        for(auto i:indices) {
            row[i[0]]++;
            col[i[1]]++;
        }
        
        int ret=0;
        
        for(int i=0;i<m;i++) {
            for(int j=0;j<n;j++) {
                ret+=(row[i]+col[j])%2;
            }
        }
        
        return ret;
    }
};
