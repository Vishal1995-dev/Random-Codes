class Solution {
public:
    vector<int> distributeCandies(int candies, int num_people) {
        vector<int> ret;
        int j=1;
        for(int i=0;i<num_people;i++) {
            if(j<=candies) {
                ret.push_back(j);
                candies-=j;
                j++;
            }
            else  {
                ret.push_back(candies);
                candies=0;
            }
        }
        int i=0;
        while(candies>0) {
            if(j<=candies) {
                ret[i]+=j;
                candies-=j;
                i++;
                j++;
                if(i==num_people) i=0;
            }
            else {
                ret[i]+=candies;
                break;
            }
        }
        return ret;
    }
};
