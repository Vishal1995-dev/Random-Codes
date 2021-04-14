class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def possible(i,j):
            return not(col[j]+hill[i-j]+dale[i+j])
        
        def place(i,j):
            queen.add((i,j))
            col[j]=1
            hill[i-j]=1
            dale[i+j]=1
        
        def remove_q(i,j):
            queen.remove((i,j))
            col[j]=0
            hill[i-j]=0
            dale[i+j]=0
        
        def add():
            sol=[]
            for _,col in sorted(queen):
                sol.append('.'*col+'Q'+'.'*(n-col-1))
            out.append(sol)
        
        def backtrack(row=0):
            for col in range(n):
                if(possible(row,col)):
                    place(row,col)
                    if(row+1==n):
                        add()
                    else:
                        backtrack(row+1)
                    remove_q(row,col)
                    
        col=[0]*n
        hill=[0]*(2*n-1)
        dale=[0]*(2*n-1)
        queen=set()
        out=[]
        backtrack()
        return out
