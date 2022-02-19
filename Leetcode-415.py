class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n1=0
        for i in num1:
            n1=n1*10+ord(i)-ord('0')
        n2=0
        for i in num2:
            n2=n2*10+ord(i)-ord('0')
        return str(n1+n2)
