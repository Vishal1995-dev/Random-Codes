class Solution {
public:
    string greedy(string s,char a,char b) {
        string ret;
        for(auto c:s) {
            if(!ret.empty() && ret.back()==a && c==b) {
                ret.pop_back();
            }
            else {
                ret.push_back(c);
            }
        }
        return ret;
    }
    
    int maximumGain(string s, int x, int y) {
        if(y>x) {
            auto s1 = greedy(s, 'b', 'a'), s2 = greedy(s1, 'a', 'b');
            return (s.size() - s1.size()) / 2 * y + (s1.size() - s2.size()) /2 * x;
        }
        
        auto s1 = greedy(s, 'a', 'b'), s2 = greedy(s1, 'b', 'a');
        return (s.size() - s1.size()) / 2 * x + (s1.size() - s2.size()) /2 * y;
    }
};
