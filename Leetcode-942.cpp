class Solution {
public:
    vector<int> diStringMatch(string S) {
        vector<int> ret;
        int i=0;
        int j=S.length();
        for(int s=0;s<S.length();s++)
        {
            if(S[s]=='I')
            {
                ret.push_back(i);
                i++;
            }
            else if(S[s]=='D')
            {
                ret.push_back(j);
                j--;
            }
        }
        ret.push_back(i);
        return ret;
    }
};
