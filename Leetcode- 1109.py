class Solution {
public:
    vector<int> corpFlightBookings(vector<vector<int>>& bookings, int n) {
        vector<int> reserved(n);
        for(vector<int> x:bookings)
        {
            reserved[x[0]-1]+=x[2];
            if(x[1]<n) reserved[x[1]]-=x[2];
        }
        for(int i=1;i<n;i++)
        {
            reserved[i]+=reserved[i-1];
        }
        return reserved;
    }
};
