class Solution(object):
    def divisorSubstrings(self, num, k):
        """
        :type num: int
        :type k: int
        :rtype: int
        """
        ret=0
        for i in range(len(str(num))-k+1):
            if(int(str(num)[i:i+k])!=0 and num%int(str(num)[i:i+k])==0):
                ret+=1
        return ret
