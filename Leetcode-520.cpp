class Solution {
public:
    bool detectCapitalUse(string word) {
        if(word.size()==1) return true;
        
        int i=(word[0]);
        if(i>=65 && i<=90) {
            int j=word[1];
            if(j>=65 && j<=90) {
                for(int p=2;p<word.size();p++) {
                    j=word[p];
                    if(j<65 || j>90) return false;
                }
            }
            else {
                for(int p=2;p<word.size();p++) {
                    j=word[p];
                    if(j>=65 && j<=90) return false;
                }
            }
        }
        else {
            for(int p=0;p<word.size();p++) {
                    int j=word[p];
                    if(j>=65 && j<=90) return false;
                }
        }
        return true;
    }
};
