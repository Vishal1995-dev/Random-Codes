class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        l=len(s)
        def fun(i):
            if(i>=l):
                return ''
            ret=''
            val=1
            i+=1
            while(val!=0):
                if(s[i]=='('):
                    val+=1
                else:
                    val-=1
                ret+=s[i]
                i+=1
            return ret[:-1] + fun(i)
        
        return fun(0)
