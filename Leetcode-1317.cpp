class Solution {
public:
    bool check(int a,int b) {
        while(a!=0) {
            int d=a%10;
            if(d==0) return false;
            a=a/10;
        }
        while(b!=0) {
            int d=b%10;
            if(d==0) return false;
            b=b/10;
        }
        return true;
    }
    
    vector<int> getNoZeroIntegers(int n) {
        vector<int> ret;
        for(int i=1;i<n;i++) {
            if(check(i,n-i)==true) return {i,n-i};
        }
        return ret;
    }
};
