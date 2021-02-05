class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        a=[]
        for i in range(1,n+1):
            a.append(i)
        
        from itertools import permutations  

        return combinations(a,k) 
