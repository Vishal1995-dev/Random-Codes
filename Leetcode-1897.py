class Solution(object):
    def makeEqual(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        d={}
        n=len(words)
        for i in words:
            for j in i:
                if(j in d):
                    d[j]+=1
                else:
                    d[j]=1
        for i in d:
            if(d[i]%n!=0):
                return False
        return True
