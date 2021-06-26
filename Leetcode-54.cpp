class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int i=0,j=0;
        int l1=1,l2=0,r2=matrix[0].size()-1,l3=matrix.size()-1;
        vector<int>ret;
        int flag=0;
        while(true) {
            if(flag==0) {
                flag=1;
                while(j<=r2) {
                    ret.push_back(matrix[i][j]);
                    j+=1;
                }
                j-=1;
                i+=1;
                r2-=1;
            }
            else if(flag==1) {
                flag=2;
                while(i<=l3) {
                    ret.push_back(matrix[i][j]);
                    i+=1;
                }
                i-=1;
                j-=1;
                l3-=1;
            }
            else if(flag==2) {
                flag=3;
                while(j>=l2) {
                    ret.push_back(matrix[i][j]);
                    j-=1;
                }
                j+=1;
                i-=1;
                l2+=1;
            }
            else if(flag==3) {
                flag=0;
                while(i>=l1) {
                    ret.push_back(matrix[i][j]);
                    i-=1;
                }
                i+=1;
                j+=1;
                l1+=1;
            }
            if(ret.size()>=matrix[0].size()*matrix.size()) break;
        }
        return ret;
    }
};
