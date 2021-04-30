class Solution {
public:
    int countSegments(string s) {
        int ret=0;
        int l=s.size();
        int i=0;
        while(i<l)
        {
            if(s[i]!=' ')
            {
                while(i<l && s[i]!=' ') i++;
                ret++;
            }
            i++;
        }
        return ret;
    }
};
