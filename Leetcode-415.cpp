class Solution {
public:
    static bool cmp(const pair<int,int> &a,const pair<int,int> &b)
    {
        return (a.second > b.second);
    }
    
    string frequencySort(string s) {
        map<char,int>m;
        vector<pair<char,int>>p;
        string ret;
        
        for(char c:s) m[c]++;
        
        for(auto i:m) p.push_back({i.first,i.second});
        
        sort(p.begin(),p.end(),cmp);
        
        for(auto i:p) {
            while(i.second>0) {
                ret+=i.first;
                i.second--;
            }    
        }
        
        return ret;
    }
};
