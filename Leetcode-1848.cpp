class Solution {
public:
    int getMinDistance(vector<int>& nums, int target, int start) {
        int s=start;
        int e=start;

        while(s>=0 || e<nums.size()) {
            if(s>=0 && nums[s]==target) return start-s;
            if(e<nums.size() && nums[e]==target) return e-start;
            s--;
            e++;
        }
        return -1;
    }
};
