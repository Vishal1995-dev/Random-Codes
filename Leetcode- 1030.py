class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        ret={}
        for i in range(R):
            for j in range(C):
                d=abs(r0-i)+abs(c0-j)
                if(d in ret):
                    ret[d].append([i,j])
                else:
                    ret[d]=[[i,j]]
        r=[]
        for i in sorted(ret.keys()):
            for j in ret[i]:
                r.append(j)
        return r
