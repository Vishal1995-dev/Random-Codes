class Solution {
public:
    int findNthDigit(int n) {
        int i=1,si=1,val=10;
        while(si<n) {
            n-=si;
            i++;
            if(i==val) {
                si++;
                val*=10;
            } 
        }
        return to_string(i)[n-1]-48;
    }
};
