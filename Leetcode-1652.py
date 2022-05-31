class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        l=len(code)
        ret=[0]*l
        if(k==0):
            return ret
        flag=0
        if(k<0):
            flag=1
            k=-k
            code=code[::-1]
        s=sum(code[1:1+k])
        for i in range(l):
            ret[i]=s
            s-=code[(i+1)%l]
            s+=code[(i+k+1)%l]
        if(flag==1):
            return ret[::-1]
        return ret
