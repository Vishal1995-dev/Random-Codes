class Solution {
public:
    vector<string> findRelativeRanks(vector<int>& score) {
        vector<int>v=score;
        sort(score.begin(),score.end());
        map<int,string>m;
        for(int i=0;i<score.size();i++) {
            if(i==score.size()-1) m[score[score.size()-1]]="Gold Medal";
            else if(i==score.size()-2) m[score[score.size()-2]]="Silver Medal";
            else if(i==score.size()-3) m[score[score.size()-3]]="Bronze Medal";
            else 
                m[score[i]]=to_string(score.size()-i);
        }
        vector<string>ret;
        for(int i=0;i<score.size();i++) {
            ret.push_back(m[v[i]]);
        }
        return ret;
    }
};
