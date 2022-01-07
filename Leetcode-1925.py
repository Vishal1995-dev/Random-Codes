class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret=0
        for i in range(1,n):
            for j in range(i,n):
                v=i*i+j*j
                p=int(math.sqrt(v))
                if(p*p==v and p<=n):
                    ret+=1
        return ret*2
