class Solution {
public:
    int largestSubmatrix(vector<vector<int>>& matrix) {
        int ret=0;
        int n = matrix.size();
        int m = matrix[0].size();
        for(int i=1;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                if(matrix[i][j]==1)
                    matrix[i][j]+=matrix[i-1][j];
            }
        }
        for(int i=0;i<n;i++)
        {
            sort(matrix[i].begin(),matrix[i].end(),greater<int>());

            for(int j=0;j<m;j++)
            {
                int a = (j+1)*(matrix[i][j]);
                if(a>ret) 
                    ret=a;
            }
        }
        return ret;
    }
};
