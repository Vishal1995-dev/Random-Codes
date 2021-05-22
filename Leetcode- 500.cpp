class Solution {
public:
    vector<string> findWords(vector<string>& words) {
        vector<string> ret;
        map<char,int> element;
        vector<string> rows = {"QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"};
        
        for(int i=0;i<3;i++) {
            for(auto j:rows[i]) {
                element.insert({j,i});
            }
        }
        for(int i=0;i<words.size();i++) {
            int flag=0;
            for(int j=0;j<words[i].size()-1;j++) {
                if(element[char(toupper(words[i][j]))]!=element[char(toupper(words[i][j+1]))]) {
                    flag=1;
                    break;
                }
            }
            if(flag==0) ret.push_back(words[i]);
        }
        return ret;
    }
};
