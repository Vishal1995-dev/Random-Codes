class Solution {
public:
    string modifyString(string s) {
        int l=s.length();
        if(l==1) {
            if(s[0]=='?') return "a";
            return s;
        }
        for(int i=1;i<s.length()-1;i++) {
            if(s[i]=='?') {
                int c=97;
                while(char(c)==s[i-1] || char(c)==s[i+1]) c++;
                s[i]=char(c);
            }
        }
        if(s[0]=='?') {
            int c=97;
            while(char(c)==s[1]) c++;
            s[0]=char(c);
        }
        
        if(s[s.length()-1]=='?') {
            int c=97;
            while(char(c)==s[s.length()-2]) c++;
            s[s.length()-1]=char(c);
        }
        
        return s;
    }
};
