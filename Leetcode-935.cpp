class Solution {
public:
    int dp[5001][10];
    vector<vector<int>>moves={{4,6},{8,6},{7,9},{4,8},{3,9,0},{},{1,7,0},{2,6},{1,3},{2,4}};
    
    long travel(int i,int n) {
        if(n==0) return 1;
        if(dp[n][i]!=-1) return dp[n][i];
        long long v=0;
        for(int j:moves[i]) v+=travel(j,n-1);
        return dp[n][i]=v%1000000007;
    }
    
    int knightDialer(int n) {
        long long ret=0;
        memset(dp,-1,sizeof(dp));
        for(int i=0;i<10;i++) {
            ret+=travel(i,n-1);
        }
        return ret%1000000007;        
    }
};
