class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        s=""
        for i in paragraph:
            if(i not in "!?',;."):
                s+=i.lower()
            else:
                s+=" "   
        s=s.split()
        d={}
        ret=""
        val=0
        for i in s:
            if(i not in banned):
                if(i not in d):
                    d[i]=1
                else:
                    d[i]+=1
                if(val<d[i]):
                    val=d[i]
                    ret=i
        return ret
