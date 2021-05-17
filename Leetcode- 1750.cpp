class Solution {
public:
    int minimumLength(string s) {
        int l=0;
        int r=s.length()-1;
        int flag=0;
        
        while(l<r && flag==0) {
            if(s[l]==s[r]) {
                char e=s[l];
                while(s[l]==e && l<r) l++;
                while(s[r]==e && l<=r) r--;
            }
            else flag=1;
        }
        return r-l+1;
    }
};
