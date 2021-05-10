class Solution {
public:
    vector<vector<int>> largeGroupPositions(string s) {
        int i=0;
        vector<vector<int>> ret;
        while(i<s.size()) {
            int j=i;
            char a=s[i];
            int c=0;
            while(s[i]==a) {
                c++;
                i++;
            }
            if(c>=3) {
                ret.push_back({j,i-1});
            }
        }
        return ret;
    }
};
