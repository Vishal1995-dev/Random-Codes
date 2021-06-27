class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        int ret=0;
        sort(people.begin(),people.end());
        int start=0;
        int end=people.size()-1;
        while(start<=end) {
            ret++;
            if(people[start]+people[end]<=limit) start++;
            end--;
        }
        return ret;
    }
};
