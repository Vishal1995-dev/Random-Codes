class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {       
        map<int,int>m;
        vector<int>c=nums;
        vector<int> ret;
        sort(c.begin(),c.end());
        for(int i=c.size()-1;i>=0;i--) {
            m[c[i]]=i;
        }
        for(int i=0;i<c.size();i++) {
            ret.push_back(m[nums[i]]);            
        }
        return ret;
    }
};
