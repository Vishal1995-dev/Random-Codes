class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        map<int,int> c;
        map<int,int> check;
        
        for(int i=0;i<arr.size();i++) {
            c[arr[i]]++;
        }
        
        for(auto i:c) {
            check[i.second]++;
            if(check[i.second]>1) return false;
        }
        
        return true;
    }
};
