class Solution {
public:
    bool judgeSquareSum(int c) {
        long int i=0;
        while(i*i<=c) {
            int d=c-i*i;
            long long root=sqrt(d);
            if(root*root==d) return true;
            i++;
        }
        return false;
    }
};
