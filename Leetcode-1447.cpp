#include<string>
class Solution {
public:
    int gcd(int a,int b)
    {
        if(b==0) return a;
        return gcd(b,a%b);
    }
    
    vector<string> simplifiedFractions(int n) {
        vector<string> ret;
        for(int i=1;i<n+1;i++)
        {
            for(int j=2;j<n+1;j++)
            {
                if(j>i && gcd(j,i)==1)
                {
                    {
                        string s=std::to_string(i)+"/"+std::to_string(j);        
                        ret.push_back(s);
                    }
                }
            }
        }
        return ret;
    }
};
