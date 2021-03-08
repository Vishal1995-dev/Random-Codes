class Solution(object):
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        A.sort()
        ret=[]
        for i in B:
            flag=0
            for j in A:
                if(j>i):
                    ret.append(j)
                    A.remove(j)
                    flag=1
                    break
            if(flag==0):
                ret.append(A[0])
                A.pop(0)
        return ret
            
