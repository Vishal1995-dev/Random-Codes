class Solution {
public:
    bool valid(string s) {
        int val=0;
        for(auto i:s) {
            if(i=='(') val+=1;
            else val-=1;
            if(val<0) return false;
        }
        return val==0;
    }
    
    void generate(string s,vector<string>& ret,int n) {
        if(s.size()==2*n) {
            if(valid(s)==true) ret.push_back(s); 
        }
        else {
            s+='(';
            generate(s,ret,n);
            s.pop_back();
            s+=')';
            generate(s,ret,n);
            s.pop_back();
        }
    }
    
    vector<string> generateParenthesis(int n) {
        string s="";
        vector<string> ret;
        generate(s,ret,n);
        return ret;
    }
};
