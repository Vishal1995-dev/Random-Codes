class Solution {
public:
    int wiggleMaxLength(vector<int>& nums) {
        int n = nums.size();
        int up[n];
        int down[n];
        up[0]=down[0]=1;
        for(int i=1;i<n;i++)
        {
            if(nums[i]>nums[i-1])
            {
                up[i]=down[i-1]+1;
                down[i]=down[i-1];
            }
            else if(nums[i]<nums[i-1])
            {
                down[i]=up[i-1]+1;
                up[i]=up[i-1];
            }
            else
            {
                down[i]=down[i-1];
                up[i]=up[i-1];
            }
        }
        if(down[n-1]<up[n-1])
        {
            return up[n-1];
        }
        return down[n-1];
    }
};
