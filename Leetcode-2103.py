class Solution(object):
    def countPoints(self, rings):
        """
        :type rings: str
        :rtype: int
        """
        ret=0
        seen=[]
        d={}
        for i in range(0,len(rings),2):
            if(rings[i+1] in d):
                if(rings[i] not in d[rings[i+1]]):
                    d[rings[i+1]]+=rings[i]
            else:
                d[rings[i+1]]=rings[i]
            if(len(d[rings[i+1]])==3):
                if(rings[i+1] not in seen):
                    ret+=1
                    seen.append(rings[i+1])
        return ret
    
