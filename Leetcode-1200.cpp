class Solution {
public:
    vector<vector<int>> minimumAbsDifference(vector<int>& arr) {
        sort(arr.begin(),arr.end());
        int m=INT_MAX;
        vector<vector<int>>ret;
        for(int i=0;i<arr.size()-1;i++) {
            if(arr[i+1]-arr[i]<m) {
                m=arr[i+1]-arr[i];
                ret.clear();
                ret.push_back({arr[i],arr[i+1]});
            }
            else if(arr[i+1]-arr[i]==m) {
                ret.push_back({arr[i],arr[i+1]});
            }
        }
        return ret;
    }
};
