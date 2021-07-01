class Solution {
public:
    bool checkPowersOfThree(int n) {
        int i=16;
        while(n>0) {
            while(pow(3,i)>n and i>=0) i--;
            if(i==-1) return false;
            n=n-pow(3,i);
            i-=1;
        }
        return true;
    }
};
