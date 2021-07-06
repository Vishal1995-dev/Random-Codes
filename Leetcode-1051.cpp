class Solution {
public:
    int heightChecker(vector<int>& heights) {
        int ret=0;
        vector<int> a=heights;
        sort(a.begin(),a.end());
        for(int i=0;i<a.size();i++) {
            if(a[i]!=heights[i]) ret++;
        }
        return ret;
    }
};
