class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        d={}
        d['L']=[-1,0]
        d['R']=[1,0]
        d['U']=[0,1]
        d['D']=[0,-1]
        
        o=[0,0]
        for i in moves:
            o[0]+=d[i][0]
            o[1]+=d[i][1]
        
        return o==[0,0]
