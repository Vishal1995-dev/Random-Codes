class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        r=len(original)
        if(r!=m*n):
            return []
        ret=[]
        x=0
        for i in range(m):
            a=[]
            for j in range(n):
                a.append(original[x])
                x+=1
            ret.append(a)
        return ret
        
