class Solution(object):
    def removeDigit(self, number, digit):
        """
        :type number: str
        :type digit: str
        :rtype: str
        """
        ret=0
        for i in range(len(number)-1,-1,-1):
            if(number[i]==digit):
                ret=max(ret,int(number[:i]+number[i+1:]))
        return str(ret)
        
