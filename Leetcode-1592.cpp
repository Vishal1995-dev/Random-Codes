class Solution {
public:
    string reorderSpaces(string text) {
        int s_c=0;
        int i=0;
        vector<string>words;
        while(i<text.length()) {
            if(text[i]==' ') {
                s_c++;
                i++;
            }
            else {
                string s;
                while(i<text.length() && text[i]!=' ') {
                    s+=text[i];
                    i++;
                }
                words.push_back(s);
            }
        }
        string ret;
        int left=0;
        if(words.size()>1) {
            left=s_c%(words.size()-1);
            int n=s_c/(words.size()-1);
            for(int i=0;i<words.size()-1;i++) {
                ret+=words[i];
                int j=0;
                while(j<n) {
                    ret+=' ';
                    j++;
                }
            }
        }
        else {
            left=s_c;
        }
        ret+=words[words.size()-1];
        while(left>0) {
            ret+=' ';
            left--;
        }
        return ret;
    }
};
