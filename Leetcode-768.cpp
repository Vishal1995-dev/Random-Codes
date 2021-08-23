class Solution {
public:
    int maxChunksToSorted(vector<int>& arr) {
        int i=0,j=0,ret=0;
        vector<int>a=arr;
        sort(a.begin(),a.end());
        while(i<arr.size()) {
            vector<int>v;
            for(int p=j;p<=i;p++) v.push_back(arr[p]);
            sort(v.begin(),v.end());
            if(v==vector(a.begin()+j,a.begin()+i+1)) {
                ret++;
                i++;
                j=i;
            }
            else i++;
        }
        return ret;
    }
};
