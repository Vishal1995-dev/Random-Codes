class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int low=0;
        int high=nums.size()-1;
        while(low<=high) {
            int mid=low+(high-low)/2;
            if(nums[mid]==target) return mid;
            else if(nums[mid]>target) {
                if(mid-1<0) return 0;
                if(mid-1>=0 && nums[mid-1]<target) return mid;
                else high=mid-1;
            }
            else {
                if(mid+1==nums.size()) return nums.size();
                if(mid+1<nums.size() && nums[mid+1]>target) return mid+1;
                else low=mid+1;
            }
        }
        return -1;
    }
};
