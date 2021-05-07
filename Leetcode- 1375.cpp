class Solution {
public:
    int numTimesAllBlue(vector<int>& light) {
        int ret=0;
        int max=0;
        for(int i=0;i<light.size();i++)
        {
            if(light[i]>max) max=light[i];
            if(max==i+1) ret++;
        }
        return ret;
    }
};
