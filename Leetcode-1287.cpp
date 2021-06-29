class Solution {
public:
    int findSpecialInteger(vector<int>& arr) {
        float l=arr.size();
        int i=0;
        while(i<l)
        {
            float c=0;
            int ele=arr[i];
            while(i<l and arr[i]==ele)
            {
                i++;
                c++;
            }
            if(c>l/4) return arr[i-1];
        }
        return arr[l-1];
    }
};
