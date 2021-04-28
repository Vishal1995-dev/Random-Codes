class Solution {
public:
    int findMinDifference(vector<string>& v) {
        sort(v.begin(),v.end());
        vector<int> a;
        
        for(string i:v)
        {
            string r1=i.substr(0,2);
            string r2=i.substr(3,2);
            int r=stoi(r1)*60+stoi(r2);
            a.push_back(r);
        }
        
        int ret=a[a.size()-1]-a[0];
        if(ret>720) ret=1440-ret;
        
        for(int i=1;i<a.size();i++)
        {
            int r1=a[i]-a[i-1];
            if(r1>720) r1=1440-r1;

            ret=std::min(r1,ret);
            
            if(ret==0) return 0;
        }
        
        return ret;
    }
};
