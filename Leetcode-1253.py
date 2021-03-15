class Solution(object):
    def reconstructMatrix(self, upper, lower, colsum):
        """
        :type upper: int
        :type lower: int
        :type colsum: List[int]
        :rtype: List[List[int]]
        """
        a1=[0]*len(colsum)
        a2=[0]*len(colsum)
        o=[]
        s1=0
        s2=0
        for i in range(len(colsum)):
            if(colsum[i]==2):
                s1+=1
                s2+=1
                a1[i]=1
                a2[i]=1
                if(s1>=upper and s2>=lower):
                    return []
            elif(colsum[i]==1):
                o.append(i)   
        for i in o:
            if(s1<upper):
                s1+=1
                a1[i]=1
            elif(s2<lower):
                s2+=1
                a2[i]=1
            else:
                return []
        if(s1!=upper or s2!=lower):
            return []
        return [a1,a2]
