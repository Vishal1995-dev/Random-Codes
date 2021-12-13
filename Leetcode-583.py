class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m=len(word1)
        n=len(word2)
        d=[]
        for i in range(m+1):
            a=[0]*(n+1)
            d.append(a)
        
        for i in range(m+1):
            for j in range(n+1):
                if(i==0 or j==0):
                    continue
                if(word1[i-1]==word2[j-1]):
                    d[i][j]=1+d[i-1][j-1]
                else:
                    d[i][j]=max(d[i][j-1],d[i-1][j])
                print(d)
        return m+n-2*d[m][n]
