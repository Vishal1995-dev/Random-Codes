class Solution {
public:
    int minStartValue(vector<int>& nums) {
        int min=INT_MAX;
        int sum=0;
        for(int i=0;i<nums.size();i++) {
            sum+=nums[i];
            if(sum<min) min=sum;
        }
        if(min<0) return -min+1;
        return 1;
    }
};
