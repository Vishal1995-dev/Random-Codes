class Solution {
public:
    int maxNumberOfBalloons(string text) {
        map<char,int> m;
        for(auto i:text) m[i]++;
        
        return min({m['b'],m['a'],m['l']/2,m['o']/2,m['n']});
    }
};
