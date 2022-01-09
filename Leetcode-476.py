class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        ret=0
        j=1
        while(num!=0):
            ret+=(j*((num&1)^1))
            j*=2
            num//=2
        return ret
