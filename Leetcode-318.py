class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        ret=0
        d={}
        for i in words:
            mask=0
            for j in i:
                mask |= (1 << (ord(j) - 97))
            d[i]=mask
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if(d[words[i]]&d[words[j]]==0 and len(words[i])*len(words[j])>ret):
                    ret=len(words[i])*len(words[j])
        return ret
                    
