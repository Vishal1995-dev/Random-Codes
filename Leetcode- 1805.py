class Solution(object):
    def numDifferentIntegers(self, word):
        """
        :type word: str
        :rtype: int
        """
        a=[]
        i=0
        while(i<len(word)):
            if(word[i].isdigit()):
                s=""
                while(i<len(word) and word[i].isdigit()):
                    s+=word[i]
                    i+=1
                s=int(s)
                a.append(s)
            else:
                i+=1
        a=set(a)
        return len(a)
