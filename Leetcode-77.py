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
        
        def n_length_combo(lst, n):
            if n == 0: 
                return [[]] 
            l =[] 
            for i in range(0, len(lst)): 
                m = lst[i] 
                remLst = lst[i + 1:]
                for p in n_length_combo(remLst, n-1):
                    l.append([m]+p) 
            return l
        
        return n_length_combo(a,k)
