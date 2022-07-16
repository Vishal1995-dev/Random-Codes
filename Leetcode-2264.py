class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        ret=""
        v=0
        i=0
        l=len(num)
        while(i<l-2):
            if(num[i]==num[i+1]==num[i+2] and int(num[i])>=v):
                ret=num[i]*3
                v=int(num[i])
            i+=1
        return ret
