class Solution {
public:
    int maxFrequency(vector<int>& nums, int k) {
        sort(nums.begin(),nums.end());
        int ret=1,i=0,j;
        long sum=0;
        for(int j=0;j<nums.size();++j) {
            sum+=nums[j];
            while(sum+k<long(nums[j])*(j-i+1)) {
                sum-=nums[i];
                i++;
            }
            if(ret<j-i+1) ret=j-i+1;
        }
        return ret;
    }
};
