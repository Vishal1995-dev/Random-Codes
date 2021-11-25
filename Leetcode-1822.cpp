class Solution {
public:
    int mod(int n)
    {
        if(n>0)
            return 1;
        return -1;
    }
    int arraySign(vector<int>& nums) {
        int s=1;
        for(int i:nums)
        {
            s=s*i;
            if(s==0)
                return 0;
            s=mod(s);
        }
        return mod(s);
    }
};
