class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {
        map<char,int> c;
        for(auto i:stones) {
            c[i]++;
        }
        int ret=0;
        for(auto i:jewels) {
            ret+=c[i];
        }
        return ret;
    }
};
