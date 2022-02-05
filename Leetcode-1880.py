class Solution(object):
    def isSumEqual(self, firstWord, secondWord, targetWord):
        """
        :type firstWord: str
        :type secondWord: str
        :type targetWord: str
        :rtype: bool
        """
        def convert(s):
            ret=0
            for i in s:
                ret=10*(ret)+(ord(i)-ord('a'))
            return ret
        
        return convert(targetWord) == convert(firstWord)+convert(secondWord)
