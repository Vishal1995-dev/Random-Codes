class Solution {
public:
    int nearestValidPoint(int x, int y, vector<vector<int>>& points) {
        int ret=-1;
        int mini=INT_MAX;
        for(int i=points.size()-1;i>=0;i--) {
            if(points[i][0]==x) {
                if(abs(points[i][1]-y)<=mini) {
                    mini=abs(points[i][1]-y);
                    ret=i;
                }
            }    
            else if(points[i][1]==y) {
                if(abs(points[i][0]-x)<=mini) {
                    mini=abs(points[i][0]-x);
                    ret=i;
                }
            }
        }
        return ret;
    }
};
