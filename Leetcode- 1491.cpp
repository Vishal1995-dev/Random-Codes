class Solution {
public:
    double average(vector<int>& salary) {
        int min=salary[0];
        int max=salary[0];
        double sum=0.0;
        int count=0;
        
        for(auto i:salary) {
            if(i<min) min=i;
            else if(i>max) max=i;
            sum+=i;
            count++;
        }
        return (sum-min-max)/(count-2);
    }
};
