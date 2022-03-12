class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        a=s.split(" ")
        l=len(a)
        b=[""]*l
        for i in a:
            b[int(i[-1])-1]=i[:-1]
        return " ".join(b)
