class Solution(object):
    def numsSameConsecDiff(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        def check(s,k,n):
            if(k==0):
                ret.append(int(s))
            else:
                f=int(s[-1])+n
                e=int(s[-1])-n
                if(f<=9):
                    check(s+str(f),k-1,n)
                if(e>=0):
                    check(s+str(e),k-1,n)
                
        ret=[]
        for i in range(1,10):
            s=str(i)
            check(s,n-1,k)
        ret=list(set(ret))
        return ret
