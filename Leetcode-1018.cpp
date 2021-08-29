class Solution {
public:
    vector<bool> prefixesDivBy5(vector<int>& nums) {
        vector<bool>ret;
        int sum=0;
        for(int j:nums) {
            sum=(sum*2+j)%5;
            ret.push_back(sum==0);
        }
        return ret;
    }
};
