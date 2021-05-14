class Solution {
public:
    int countMatches(vector<vector<string>>& items, string ruleKey, string ruleValue) {
        int ret=0;
        int val=0;
        if(ruleKey=="color") val=1;
        if(ruleKey=="name") val=2;
        
        for(auto i:items) {
            if(i[val]==ruleValue) ret++;
        }
        return ret;
    }
};
