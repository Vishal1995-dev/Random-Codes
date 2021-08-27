class Solution {
public:
    string minWindow(string s, string t) {
        map<char,int>m;
        for(char i:t) {
            m[i]++;
        }
        int len=m.size();
        int l=0,r=0,f=0;
        map<char,int>d;
        int val=9999999;
        int left=-1;
        int right=-1;
        while(r<s.size()) {
            d[s[r]]++;
            if(m[s[r]]!=0 && m[s[r]]==d[s[r]]) f+=1;
            while(l<=r and f==len) {
                if(r-l+1<val) {
                    val=r-l+1;
                    left=l;
                    right=r;
                }
                d[s[l]]--;
                if(m[s[l]]!=0 && d[s[l]]<m[s[l]]) f--;
                l++;
            }
            r++;
        }
        if(val!=9999999) return s.substr(left,val);
        return "";
    }
};
