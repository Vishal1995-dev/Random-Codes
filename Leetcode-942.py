class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        i=0
        j=len(S)
        ret=[]
        for s in S:
            if(s=='I'):
                ret.append(i)
                i+=1
            if(s=='D'):
                ret.append(j)
                j-=1
        ret.append(i)
        return ret
