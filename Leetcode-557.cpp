class Solution {
public:
    string reverseWords(string s) {
        int i=s.size()-1;
        vector<string> v;
        while(i>=0) {
            string st;
            while(i>=0 && s[i]!=' ') {
                st+=s[i];
                i--;
            }
            v.push_back(st);
            i--;
        }
        string ret;
        for(int i=v.size()-1;i>=1;i--) {
            ret+=v[i]+' ';
        }
        ret+=v[0];
        return ret;
    }
};
