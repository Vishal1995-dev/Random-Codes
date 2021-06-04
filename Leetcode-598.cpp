class Solution {
public:
    int maxCount(int m, int n, vector<vector<int>>& ops) {
        for(vector<int> i:ops) {
            if(i[0]<m) m=i[0];
            if(i[1]<n) n=i[1];
        }
        return m*n;
    }
};
