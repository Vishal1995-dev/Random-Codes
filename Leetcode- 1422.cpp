class Solution {
public:
    int maxScore(string s) {
        int l = s.length();
        int a[l];
        int c=0;
        for(int i=l-1;i>=0;i--)
        {
            if(s[i]=='1') c++;
            a[i]=c;
        }
        int ret=0;
        c=0;
        for(int i=0;i<l-1;i++)
        {
            if(s[i]=='0') c++;
            if(ret<c+a[i+1]) ret=c+a[i+1];
        }
        return ret;
    }
};
