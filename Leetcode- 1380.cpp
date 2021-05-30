class Solution {
public:
    vector<int> luckyNumbers (vector<vector<int>>& matrix) {
        map<int,int> ma;
        vector<int> ret;
        
        int n=matrix.size();
        int m=matrix[0].size();
        
        for(int i=0;i<n;i++) {
            int min=100000;
            for(int j=0;j<m;j++) {
                if(min>matrix[i][j]) min=matrix[i][j];
            }
            ma[min]++;
        }
        
        for(int i=0;i<m;i++) {
            int max=0;
            for(int j=0;j<n;j++) {
                if(max<matrix[j][i]) max=matrix[j][i];
            }
            if(ma[max]==1) ret.push_back(max);
        }
        
        return ret;
    }
};
