class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        ret=0
        a=text.split(" ")
        for i in a:
            flag=0
            for j in brokenLetters:
                if(j in i):
                    flag=1
                    break
            if(flag==0):
                ret+=1
        return ret
            
