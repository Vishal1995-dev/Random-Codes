class Solution(object):
    def stoneGameVI(self, a, b):
        """
        :type aliceValues: List[int]
        :type bobValues: List[int]
        :rtype: int
        """
        l=len(a)
        v=[0]*l
        d={}
        for i in range(l):
            val=a[i]+b[i]
            v[i]=val
            if(val in d):
                d[val].append(i)
            else:
                d[val]=[i]
        s1=0
        s2=0
        v.sort(reverse=True)
        for i in range(l):
            m=d[v[i]].pop(0)
            if(i%2==0):
                s1+=a[m]
            else:
                s2+=b[m]
        if(s1>s2):
            return 1
        elif(s1<s2):
            return -1
        return 0
