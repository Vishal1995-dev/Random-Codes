class Solution {
public:
    int findShortestSubArray(vector<int>& nums) {
        map<int,int> count;
        map<int,int>start;
        map<int,int>end;
        
        for(int i=0;i<nums.size();i++)
        {
            count[nums[i]]++;
            end[nums[i]]=i;
            if(start.find(nums[i])==start.end()) start[nums[i]]=i; 
        }
        
        int max=0;
        for(auto i:count)
        {
            if(i.second>max) max=i.second;
        }
        
        int ret=nums.size();
        for(auto i:count)
        {
            if(i.second == max)
            {
                if(ret>end[i.first]-start[i.first]+1) ret=end[i.first]-start[i.first]+1;
            }
        }
        
        return ret;
    }
};
