class Solution(object):
    def rearrangeCharacters(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: int
        """
        d1={}
        d2={}
        for i in s:
            if(i in d1):
                d1[i]+=1
            else:
                d1[i]=1
        for i in target:
            if(i in d2):
                d2[i]+=1
            else:
                d2[i]=1
        ret=9999999
        for i in d2:
            if(i in d1):
                ret=min(ret,d1[i]//d2[i])
            else:
                return 0
        return ret
