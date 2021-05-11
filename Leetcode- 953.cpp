class Solution {
public:
    bool isAlienSorted(vector<string>& words, string order) {
        map<char,int> r;
        for(int i=0;i<order.size();i++) r.insert({order[i],i});
        
        for(int i=1;i<words.size();i++) {
            int j=0;
            while(j<std::min(words[i].size(),words[i-1].size())) {
                if(r[words[i][j]]<r[words[i-1][j]]) return false;
                else if(words[i][j]==words[i-1][j]) j+=1;
                else break;
            }
            if(j==words[i].size() && words[i]!=words[i-1]) return false;
        }
        return true;
    }
};
