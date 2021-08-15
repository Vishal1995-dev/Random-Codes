class Solution {
public:
    string customSortString(string order, string s) {
        map<char,int>m;
        for(char i:s) {
            m[i]++;
        }
        string ret;
        for(char i:order) {
            while(m[i]>0) {
                ret+=i;
                m[i]--;
            }
            m.erase(i);
        }
        for(auto i:m) {
            while(i.second>0) {
                ret+=i.first;
                i.second--;
            }
        }
        return ret;
    }
};
