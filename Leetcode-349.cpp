class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        map<int,int> m;
        vector<int> ret;
        for(auto i:nums1) {
            m[i]++;
        }
        for(auto i:nums2) {
            if(m[i]!=0) {
                ret.push_back(i);
                m[i]=0;
            }
        }
        return ret;
    }
};
