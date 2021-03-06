class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        a=list(sentence.split(" "))
        j=0
        for i in a:
            j+=1
            if(len(i)>=len(searchWord)):
                if(i[:len(searchWord)]==searchWord):
                    return j
        if(j>=len(a)):
            return -1
            
