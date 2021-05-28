class Solution {
public:
    bool find(vector<vector<int>> queens,vector<int> a){
        for(auto i:queens) {
            if(i==a) return true;
        }
        return false;
    }
    vector<vector<int>> queensAttacktheKing(vector<vector<int>>& queens, vector<int>& king) {
        vector<vector<int>> ret;
        
        int i=king[0]-1;
        int j=king[1]-1;
        while(i>=0 and j>=0){
            if(find(queens,{i,j})==true){
                ret.push_back({i,j});
                break;
                }
            i-=1;
            j-=1;   
            }
        
        i=king[0]+1;
        j=king[1]+1;
        while(i<8 and j<8){
            if(find(queens,{i,j})==true){
                ret.push_back({i,j});
                break;
                }
            i+=1;
            j+=1;   
            }
        
        i=king[0]+1;
        j=king[1]-1;
        while(i<8 and j>=0){
            if(find(queens,{i,j})==true){
                ret.push_back({i,j});
                break;
                }
            i+=1;
            j-=1;  
            }
        
        i=king[0]-1;
        j=king[1]+1;
        while(i>=0 and j<8){
            if(find(queens,{i,j})==true){
                ret.push_back({i,j});
                break;
                }
            i-=1;
            j+=1;   
            }
        
        j=king[1];
        for(int i=king[0];i<8;i++) {
            if(find(queens,{i,j})==true){
                ret.push_back({i,j});
                break;
            }
        }
        for(int i=king[0];i>=0;i--) {
            if(find(queens,{i,j})==true){
                ret.push_back({i,j});
                break;
            }
        }
        j=king[0];
        for(int i=king[1];i<8;i++) {
            if(find(queens,{j,i})==true){
                ret.push_back({j,i});
                break;
            }
        }
        for(int i=king[1];i>=0;i--) {
            if(find(queens,{j,i})==true){
                ret.push_back({j,i});
                break;
            }
        }
        return ret;
    }
};
