class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        a=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        d={}
        for i in words:
            s=""
            for j in i:
                s+=a[ord(j)-ord('a')]
            if(s not in d):
                d[s]=1
        return len(d)
