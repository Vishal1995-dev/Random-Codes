class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int l=heights.size();
        vector<int>left(l);
        vector<int>right(l);
        right[l-1]=l;
        left[0]=-1;
        
        for(int i=1;i<l;i++) {
            int p=i-1;
            while(p>=0 && heights[p]>=heights[i]) p=left[p];
            left[i]=p;
        }
        
        for(int i=l-2;i>=0;i--) {
            int p=i+1;
            while(p<l && heights[p]>=heights[i]) p=right[p];
            right[i]=p;
        }
        
        int ret=0;
        for(int i=0;i<l;i++) {
            if(ret<heights[i]*(-left[i]+right[i]-1)) ret=heights[i]*(-left[i]+right[i]-1);
        }
        
        return ret;
    }
};
