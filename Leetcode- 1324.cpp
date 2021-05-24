class Solution {
public:
    vector<string> printVertically(string s) {
        vector<string> a;
        vector<int> l;
        int max=0;
        
        string word = "";
        int len=0;
        for (auto x : s) {
            if (x == ' ') {
                a.push_back(word);
                l.push_back(len);
                if(len>max) max=len;
                word = "";
                len=0;
            }
            else {
                word = word + x;
                len++;
            }
        }
        if(len>max) max=len;
        a.push_back(word);
        l.push_back(len);
        
        vector<string> ret;
        for(int j=0;j<max;j++) {
            string s="";
            for(int i=0;i<a.size();i++) {
                if(j>=l[i]) s+=" ";
                else s+=a[i][j];
            }
            while(s[s.size()-1]==' ') s=s.substr(0,s.size()-1); 
            ret.push_back(s);
        }
        return ret;
    }
};
