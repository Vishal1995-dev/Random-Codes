class Solution {
public:
    string makeGood(string s) {
        int flag=0;
        while(flag==0 and s.length()>0)
        {
            flag=1;
            for(int i=0;i<s.length()-1;i++)
            {
                if(int(s[i])-int(s[i+1])==32 or int(s[i])-int(s[i+1])==-32)
                {
                    s.erase(i,2);
                    flag=0;
                    break;
                }
            }
        }
        return s;
    }
};
