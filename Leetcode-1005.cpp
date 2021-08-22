class Solution {
public:
    int largestSumAfterKNegations(vector<int>& nums, int k) {
        sort(nums.begin(),nums.end());
        int i=0;
        while(k>0 && i<nums.size() && nums[i]<0) {
            nums[i]=-nums[i];
            k--;
            i++;
        }
        sort(nums.begin(),nums.end());
        if(k%2!=0) nums[0]=-nums[0];
        int ret=0;
        for(int j:nums) {
            ret+=j;
        }
        
        return ret;
    }
};
