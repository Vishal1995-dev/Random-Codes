class Solution {
public:
    bool backspaceCompare(string s, string t) {
        vector<int> v1;
        vector<int> v2;
        
        for(auto i:s) {
            if(i=='#') {
                if(v1.size()>0) v1.pop_back();
            }
            else v1.push_back(i);
        }
        
        for(auto i:t) {
            if(i=='#') {
                if(v2.size()>0) v2.pop_back();
            }
            else v2.push_back(i);
        }
        
        return v1==v2;
    }
};
