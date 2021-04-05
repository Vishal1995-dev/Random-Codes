class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
        if(pushed.size()==0) return true;
        vector<int> a;
        while(pushed.size()!=0 or a.size()!=0)
        {
            if(a.size()==0)
            {
                a.push_back(pushed[0]);
                pushed.erase(pushed.begin());
            }
            while(a.back()!=popped[0] and pushed.size()!=0)
            {
                a.push_back(pushed[0]);
                pushed.erase(pushed.begin());
            }
            if(a.back()!=popped[0]) return false;
            a.pop_back();
            popped.erase(popped.begin());
        }
        return true;
    }
};
