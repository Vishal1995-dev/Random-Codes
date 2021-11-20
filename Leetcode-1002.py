class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        l=len(words)
        m={}
        for j in words[0]:
            if(j in m):
                m[j]+=1
            else:
                m[j]=1
        for i in words:
            for j in m:
                m[j]=min(m[j],i.count(j))
        
        ret=[]
        for i in m:
            while(m[i]!=0):
                m[i]-=1
                ret+=str(i)
        return ret
