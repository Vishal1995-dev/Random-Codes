class Solution {
public:
    double trimMean(vector<int>& arr) {
        sort(arr.begin(),arr.end());
        int s=arr.size();
        double sum=0;
        int n=s/20;
        for(int i=n;i<s-n;i++)
        {
            sum=sum+arr[i];
        }
        double ret;
        ret=(sum)/(s-2*n);
        return ret;
    }
};
