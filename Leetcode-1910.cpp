class Solution {
public:
    string removeOccurrences(string s, string part) {
        bool flag=true;
        while(flag) {
            flag=false;
            int i=0;
            int l=part.size();
            while(i<s.size() && s.size()>=l && s.size()-i>=l) {
                if(s.substr(i,l)==part) {
                    s.erase(i,l);
                    flag=true;
                    break;
                }
                i++;
            }
        }
        return s;
    }
};
