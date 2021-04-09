class Solution {
public:
    bool threeConsecutiveOdds(vector<int>& arr) {
        int ret=0;
        for(int i:arr)
        {
            if(i%2==0) ret=0;
            else ret+=1;
            if(ret==3) return true;
        }
        return false;
    }
};
