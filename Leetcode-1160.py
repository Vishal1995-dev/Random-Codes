class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        ret=0
        d={}
        for i in chars:
            if(i in d):
                d[i]+=1
            else:
                d[i]=1
        for i in words:
            flag=0
            for j in i:
                if(j not in d or i.count(j)>d[j]):
                    flag=1
                    break
            if(flag==0):
                ret+=len(i)
        return ret
                
