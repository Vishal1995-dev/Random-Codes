class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        vector<int> dp(amount+1, 999999);
        dp[0]=0;
        for(int i=0;i<amount+1;i++)
        {
            int m = dp[i];
            for(int j:coins)
            {
                if(i-j>=0 && m>1+dp[i-j]) m=dp[i-j]+1;
            }
            dp[i]=m;
        }
        if(dp[amount]==999999) return -1;
        return dp[amount];
    }
};
