class Solution {
public:
    long int kadane(vector<int> arr)
    {
        long int max_till_now=0;
        long int max_here=0;
        for(int i:arr)
        {
            max_here+=i;
            if(max_till_now<max_here) max_till_now=max_here;
            if(max_here<0) max_here=0;
        }
        return max_till_now;
    }
    
    int kConcatenationMaxSum(vector<int>& arr, int k) {
        long int s=0;
        for(int i:arr)
        {
            s+=i;
        }
        if(s<0) s=0;
        if(k>1) 
        {
            arr.insert( arr.end(), arr.begin(), arr.end() );
            return (((k-2)*s+kadane(arr))%(1000000007));
        }
        else return kadane(arr)%(1000000007);
    }
};
