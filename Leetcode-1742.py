class Solution(object):
    def countBalls(self, l, h):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """
        def fun(n):
            ret=0
            while(n):
                ret+=n%10
                n//=10
            return ret
        
        d={}
        ret=0
        for i in range(l,h+1):
            s=fun(i)
            if(s in d):
                d[s]+=1
            else:
                d[s]=1
            ret=max(ret,d[s])
        return ret
