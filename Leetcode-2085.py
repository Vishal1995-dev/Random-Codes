class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        d={}
        l=len(words1)
        for i in words1:
            if(i in d):
                d[i]=l+1
            else:
                d[i]=1
        for i in words2:
            if(i in d):
                if(d[i]==1):
                    d[i]=0
                else:
                    d[i]=l+1
        ret=0
        for i in d:
            if(d[i]==0):
                ret+=1
        return ret
        
        
