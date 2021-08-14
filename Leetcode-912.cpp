class Solution {
public:
    void swap(int *a,int *b)
    {
        int t=*a;
        *a=*b;
        *b=t;
    }
    
    int partition(vector<int> &arr,int low,int high)
    {
        int pivot=arr[high];
        int i=low-1;
        for (int j = low; j <= high - 1; j++)
        {
            if (arr[j] < pivot)
            {
                i++;
                swap(&arr[i], &arr[j]);
            }
        }
    swap(&arr[i + 1], &arr[high]);
    return (i + 1);
    }
    
    void quicksort(vector<int> &arr,int low,int high)
    {
        if(low<high)
        {
            int p = partition(arr,low,high);
            quicksort(arr,low,p-1);
            quicksort(arr,p+1,high);
        }
    }
    
    vector<int> sortArray(vector<int>& nums) {
        quicksort(nums,0,nums.size()-1);
        return nums;
    }
};
