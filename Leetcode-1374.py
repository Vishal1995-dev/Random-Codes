class Solution(object):
    def generateTheString(self, n):
        """
        :type n: int
        :rtype: str
        """
        s=""
        for i in range(n-1):
            s+="a"
        if(n%2==0):
            s+="b"
        else:
            s+="a"
        return s
