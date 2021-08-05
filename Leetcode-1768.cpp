class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string ret;
        int i=0;
        int j=0;
        if(word1.size()>word2.size()) {
            while(j<word2.size()) {
                ret+=word1[i];
                ret+=word2[j];
                i++;
                j++;
            }
            while(i<word1.size()) {
                ret+=word1[i];
                i++;
            }
        }
        else {
            while(i<word1.size()) {
                ret+=word1[i];
                ret+=word2[j];
                i++;
                j++;
            }
            while(j<word2.size()) {
                ret+=word2[j];
                j++;
            }
        }
        return ret;
    }
};
