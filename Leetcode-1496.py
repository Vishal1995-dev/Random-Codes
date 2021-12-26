class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        seen={}
        seen[(0,0)]=1
        d={}
        d['E']=[1,0]
        d['W']=[-1,0]
        d['N']=[0,1]
        d['S']=[0,-1]
        a=0
        b=0
        for i in path: 
            a+=+d[i][0]
            b+=d[i][1]
            if((a,b) in seen):
                return True
            seen[(a,b)]=1
        return False
