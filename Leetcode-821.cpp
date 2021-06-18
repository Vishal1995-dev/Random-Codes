class Solution {
public:
    vector<int> shortestToChar(string s, char c) {
        vector<int> ret;
        for(int i=0;i<s.size();i++) {
            int start=i;
            int end=i;
            while(true) {
                if(start>=0 && s[start]==c) {
                    ret.push_back(i-start);
                    break;
                }
                if(end<s.size() && s[end]==c) {
                    ret.push_back(end-i);
                    break;
                }
                start--;
                end++;
            }
        }
        return ret;
    }
};
