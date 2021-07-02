class Solution {
public:
    int binary(int n) {
        int count = 0;
        while (n) {
            count += n & 1;
            n >>= 1;
        }
        return count;
    }
    
    int countPrimeSetBits(int left, int right) {
        int ret=0;
        vector<int> a={ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29 };
        for(int i=left;i<=right;i++) {
            int n=binary(i);
            for(int j:a) {
                if(n==j) ret++;
            }
        }
        return ret;
    }
};
