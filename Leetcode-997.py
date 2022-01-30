class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        judge=-1
        if(n==1):
            return 1
        if(len(trust)==0):
            return -1
        d={}
        for i in trust:
            if(i[1] in d and d[i[1]]!=-1):
                d[i[1]]+=1
            if(i[1] not in d):
                d[i[1]]=1
            if(i[0] in d):
                d[i[0]]=-1
            else:
                d[i[0]]=-1
        for i in d:
            if(d[i]==n-1):
                return i
        return -1
            
