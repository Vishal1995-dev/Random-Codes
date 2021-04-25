class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        a=set(word1)
        
        r={}
        for i in a:
            c=word1.count(i)
            if(c in r):
                r[c]+=1
            else:
                r[c]=1
        for i in a:
            c=word2.count(i)
            if(c in r):
                r[c]-=1
            else:
                r[c]=1
        for i in r:
            if(r[i]!=0):
                return False
        return True
