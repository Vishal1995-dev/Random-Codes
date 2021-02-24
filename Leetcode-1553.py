class Solution(object):
    s=0
    def minDays(self, m):
        """
        :type n: int
        :rtype: int
        """
        self.s=999999999
        
        def eat(n,c):
            if(n==0):
                self.s=min(self.s,c)
                return
            if(n%2==0):
                eat(n//2,c+1)
            if(n%3==0):
                eat(n//3,c+1)
            eat(n-1,c+1)
            
        eat(m,0)
        return(self.s)
