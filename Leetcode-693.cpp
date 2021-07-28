class Solution {
public:
    bool hasAlternatingBits(int n) {
        int i=n%2;
        n/=2;
        while(n!=0) {
            if(i==n%2) return false;
            i=n%2;
            n/=2;
        }
        return true;
    }
};
