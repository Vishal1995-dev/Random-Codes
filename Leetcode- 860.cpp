class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        int arr[]={0,0};
        for(int i=0;i<bills.size();i++)
        {
            if(bills[i]==5) arr[0]+=1;
            else if(bills[i]==10)
            {
                if(arr[0]==0) return false;
                else
                {
                    arr[0]-=1;
                    arr[1]+=1;
                }
            }
            else
            {
                if(arr[1]>0 && arr[0]>0)
                {
                    arr[0]-=1;
                    arr[1]-=1;
                }
                else if(arr[1]==0 && arr[0]>=3) arr[0]-=3;
                else return false;
            }
        }
        return true;
    }
};
