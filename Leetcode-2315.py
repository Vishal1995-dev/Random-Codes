class Solution(object):
    def countAsterisks(self, s):
        """
        :type s: str
        :rtype: int
        """
        c=0
        ret=0
        for i in s:
            if(i=='*' and c%2==0):
                ret+=1
            if(i=='|'):
                c+=1
        return ret
