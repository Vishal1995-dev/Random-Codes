class Solution {
public:
    int longestBeautifulSubstring(string word) {
        int ret=0;
        int i=0;
        while(i<word.size()) {
            int val=0;
            if(i<word.size() && word[i]=='a') {
                while(i<word.size() && word[i]=='a') {
                    i++;
                    val++;
                }
                if(i<word.size() && word[i]=='e') {
                    while(i<word.size() && word[i]=='e') {
                        i++;
                        val++;
                    }
                    if(i<word.size() && word[i]=='i') {
                        while(i<word.size() && word[i]=='i') {
                            i++;
                            val++;
                        }
                        if(i<word.size() && word[i]=='o') {
                            while(i<word.size() && word[i]=='o') {
                                i++;
                                val++;
                            }
                            if(i<word.size() && word[i]=='u') {
                                while(i<word.size() && word[i]=='u') {
                                    i++;
                                    val++;
                                }
                                if(val>ret) ret=val;
                            }
                        }
                    }
                }
            }
            else i++;
        }
        return ret;
    }
};
