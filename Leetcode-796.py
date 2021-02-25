class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        a=list(A)
        b=list(B)
        
        if(set(a)!=set(B)):
            return False
        
        if(len(A)!=len(B)):
            return False
        
        if(len(A)==0):
            return True
        
        p=[i for i,val in enumerate(B) if val==A[0]]
        
        for i in p:
            s=B[i:]+B[0:i]
    
            if(s==A):
                return True
        return False
