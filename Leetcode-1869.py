class Solution(object):
    def checkZeroOnes(self, s):
        """
        :type s: str
        :rtype: bool
        """
        one=0
        zero=0
        i=0
        l=len(s)
        while(i<l):
            if(s[i]=='1'):
                val=0
                while(i<l and s[i]=='1'):
                    val+=1
                    i+=1
                one=max(one,val)
            else:
                val=0
                while(i<l and s[i]=='0'):
                    val+=1
                    i+=1
                zero=max(zero,val)
        return one>zero
