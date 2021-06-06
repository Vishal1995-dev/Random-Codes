class Solution {
public:
    bool checkPerfectNumber(int num) {
        int ret=0;
        for(int i=1;i*i<=num;i++) {
            if(num%i==0) {
                ret+=i;
                if(i*i!=num) ret+=num/i;
            }
        }
        return num*2==ret;
    }
};
