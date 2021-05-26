class Solution {
public:
    int repeatedNTimes(vector<int>& nums) {
        map<int,int> a;
        for(auto i : nums) {
            a[i]++;
            if(a[i]==2) return i;
        }
        return 0;
    }
};
