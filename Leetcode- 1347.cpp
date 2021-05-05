class Solution {
public:
    int minSteps(string s, string t) {
        map<char,int> r;
        for(char c:s)
        {
            r[c]++;
        }
        for(char c:t)
        {
            if(r.find(c)!=r.end())
            {
                r[c]--;
            }
        }
        int ret=0;
        for(auto i:r)
        {
            if(i.second>0) ret+=i.second;
        }
        return ret;
    }
};
