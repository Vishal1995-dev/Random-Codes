class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        c_min=0
        c_max=0
        for i in s:
            if(i=='('):
                c_min+=1
                c_max+=1
            elif(i==')'):
                c_max-=1
                c_min=max(c_min-1,0)
            elif(i=='*'):
                c_max+=1
                c_min=max(c_min-1,0)
            if(c_max<0):
                return False
        return c_min==0
