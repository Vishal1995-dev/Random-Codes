class Solution(object):
    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """
        ret=0
        s=word
        while(word in sequence):
            ret+=1
            word+=s
        return ret
