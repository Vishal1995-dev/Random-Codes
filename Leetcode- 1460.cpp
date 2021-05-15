class Solution {
public:
    bool canBeEqual(vector<int>& target, vector<int>& arr) {
        /*map<int,int> a;
        for(auto i:target) a[i]++;
        for(auto i:arr) a[i]--;
        for(auto i:a) {
            if(i.second!=0) return false;
        }
        return true;*/
        sort(target.begin(),target.end());
        sort(arr.begin(),arr.end());
        return arr==target;
    }
};
