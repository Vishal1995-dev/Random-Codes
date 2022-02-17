class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        i=0
        j=0
        for i in range(8):
            flag=0
            for j in range(8):
                if(board[i][j]=='R'):
                    flag=1
                    break
            if(flag==1):
                break
        ret=0
        s=i
        while(s>=0):
            if(board[s][j]=='p'):
                ret+=1
                break
            elif(board[s][j]=='B'):
                break
            s-=1
        s=i
        while(s<8):
            if(board[s][j]=='p'):
                ret+=1
                break
            elif(board[s][j]=='B'):
                break
            s+=1
        s=j
        while(s>=0):
            if(board[i][s]=='p'):
                ret+=1
                break
            elif(board[i][s]=='B'):
                break
            s-=1
        s=j    
        while(s<8):
            if(board[i][s]=='p'):
                ret+=1
                break
            elif(board[i][s]=='B'):
                break
            s+=1
        return ret
