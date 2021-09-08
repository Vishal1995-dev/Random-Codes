class Solution {
public:
    int numEquivDominoPairs(vector<vector<int>>& dominoes) {
        map<pair<int,int>,int>m;
        int ret=0;
        for(auto i:dominoes) {
            if(i[0]>i[1]) {
                m[{i[1],i[0]}]++;
            }
            else m[{i[0],i[1]}]++;
        }
        for(auto i:m) {
            ret+=i.second*(i.second-1)/2;
        }
        return ret;   
    }
};
