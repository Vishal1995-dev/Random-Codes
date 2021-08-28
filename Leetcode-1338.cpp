class Solution {
public:
    bool static cmp(pair<int, int>& a,pair<int, int>& b)
    {
        return a.second > b.second;
    }
    
    int minSetSize(vector<int>& arr) {
        map<int,int>m;
        for(int i:arr) m[i]++;
        vector<pair<int, int> > A;
        for (auto& it : m) {
            A.push_back(it);
        }
        sort(A.begin(), A.end(), cmp);
        int l=arr.size();
        int ret=0;
        int left=l;
        int i=0;
        while(left>l/2) {
            ret++;
            left-=A[i].second;
            i++;
        }
        return ret;
    }
};
