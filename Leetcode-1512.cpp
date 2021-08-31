class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        int ret=0;
        map<int,int>m;
        for(int i:nums) m[i]++;
        for(auto i:m) {
            if(i.second>1) ret+=i.second*(i.second-1)/2;
        }
        return ret;
    }
};
