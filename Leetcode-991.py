class Solution(object):
    def brokenCalc(self, X, Y):
        """
        :type X: int
        :type Y: int
        :rtype: int
        """
        ret=0
        while(X<Y):
            ret+=1
            if(Y%2==1):
                Y+=1
            else:
                Y/=2
        return ret+X-Y
        
