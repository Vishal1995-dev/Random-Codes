class Solution {
    public int findLongestChain(int[][] pairs) {
        Arrays.sort(pairs,(a,b)->a[0]-b[0]);
        int n=pairs.length;
        int[] dp=new int[n];
        Arrays.fill(dp,1);
        
        for(int j=1;j<n;j++)
        {
            for(int i=0;i<j;i++)
            {
                if(pairs[i][1]<pairs[j][0])
                    dp[j]=Math.max(dp[j],dp[i]+1);
            }
        }
        
        int ans=0;
        for(int x:dp) if (x>ans) ans=x;
        return ans;
    }
}
