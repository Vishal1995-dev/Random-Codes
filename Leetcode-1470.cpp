class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {
        vector<int>ret;
        int i=0;
        int j=n;
        bool flag=true;
        while(j<2*n) {
            if(flag==true) {
                flag=false;
                ret.push_back(nums[i]);
                i++;
            }
            else {
                flag=true;
                ret.push_back(nums[j]);
                j++;
            }
        }
        return ret;
    }
};
