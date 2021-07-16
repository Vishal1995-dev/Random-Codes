class Solution {
public:
    string maximumTime(string time) {
        string ret;
        string l0=time.substr(0,2);
        string l1=time.substr(3,5);
        if(l0[0]!='0') {
            for(int i=23;i>9;i--) {
                string s=to_string(i);
                if((l0[0]=='?' || l0[0]==s[0]) && (l0[1]=='?' || l0[1]==s[1])) {
                    ret+=s;
                    break;
                    }
                }
            }
        else if(l0[1]=='?')
            ret+="09";
        else
            ret+=l0;
        ret+=':';
        if(l1[0]!='0') {
            for(int i=59;i>9;i--) {
                string s=to_string(i);
                if((l1[0]=='?' || l1[0]==s[0]) && (l1[1]=='?' || l1[1]==s[1])) {
                    ret+=s;
                    break;
                    }
                }
            }
        else if(l1[1]=='?')
            ret+="09";
        else
            ret+=l1;
        return ret;
    }
};
