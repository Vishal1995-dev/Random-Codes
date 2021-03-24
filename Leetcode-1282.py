class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        ret=[]
        a={}
        p=0
        for i in groupSizes:
            if(i not in a):
                a[i]=[p]
            else:
                a[i].append(p)
            p+=1
        for i in a:
            while(a[i]):
                j=i
                r=[]
                while(j>0):
                    r.append(a[i][0])
                    a[i].pop(0)
                    j-=1
                ret.append(r)
        return ret
