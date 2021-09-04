class Solution {
public:
    int live(vector<vector<int>>&board,int i,int j,int m,int n) {
        int lives=0;
        for(int p=max(i-1,0);p<min(i+2,m);p++) {
            for(int q=max(j-1,0);q<min(j+2,n);q++) {
                lives+=(board[p][q]&1);
            }
        }
        lives-=(board[i][j]&1);
        return lives;
    }
    
    void gameOfLife(vector<vector<int>>& board) {
        int m=board.size();
        int n=board[0].size();
        
        for(int i=0;i<m;i++) {
            for(int j=0;j<n;j++) {
                int lives=live(board,i,j,m,n);
                if(board[i][j]==0 && lives==3) {
                    board[i][j]+=2;
                }
                else if(board[i][j]==1 && lives>=2 && lives<=3) {
                    board[i][j]+=2;
                }
            }
        }
        
        for(int i=0;i<m;i++) {
            for(int j=0;j<n;j++) {
                board[i][j]>>=1;
            }
        }
        
        return;
    }
};
