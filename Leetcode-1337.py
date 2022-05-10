class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        d={}
        for i in range(len(mat)):
            ret=sum(mat[i])
            if(ret in d):
                d[ret].append(i)
            else:
                d[ret]=[i]
        ret=[]
        for key in sorted(d):
            while(k>0 and len(d[key])!=0):
                ret.append(d[key].pop(0))
                k-=1
        return ret
        
