class Solution(object):
    def dailyTemperatures(self, t):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        l=len(t)
        ret=[0]*l
        s=[]
        for i,j in enumerate(t):
            while(s and t[s[-1]]<j):
                val=s.pop()
                ret[val]=i-val
            s.append(i)
        return ret
