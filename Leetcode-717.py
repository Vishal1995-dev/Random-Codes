class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        l=len(bits)
        if(l==1):
            return True
        i=l-2
        if(bits[i]==0):
            return True
        else:
            while(i>=0 and bits[i]==1):
                i-=1
            return((l-2-i)%2==0)
