class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {
        int ret=0;
        map<char,int>j;
        for(char i:jewels) j[i]=1;
        for(char i:stones) {
            ret+=j[i];
        }
        return ret;
    }
};
