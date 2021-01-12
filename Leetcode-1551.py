class Solution(object):
    def minOperations(self, n):
        """
        :type n: int
        :rtype: int
        
        s=1
        i=1
        a=n
        while(n>1):
            s+=2*i+1 
            i+=1
            n-=1
        s=s/a
        """
        s=n
        j=1
        i=0
        ret=0
        while(i<n/2):
            ret+=s-j
            j+=2
            i+=1
        return ret
