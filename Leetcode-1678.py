class Solution(object):
    def interpret(self, c):
        """
        :type command: str
        :rtype: str
        """
        i=0
        ret=""
        l=len(c)
        while(i<l):
            if(c[i]=='('):
                if(c[i+1]==')'):
                    ret+='o'
                    i+=2
                else:
                    ret+="al"
                    i+=4
            else:
                ret+='G'
                i+=1
        return ret
