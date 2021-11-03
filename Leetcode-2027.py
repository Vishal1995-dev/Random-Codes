class Solution(object):
    def minimumMoves(self, s):
        """
        :type s: str
        :rtype: int
        """
        i=0
        ret=0
        s=list(s)
        while(i<len(s)):
            if(s[i]=='X'):
                s[i]='O'
                if(i+1<len(s)):
                    s[i+1]='O'
                if(i+2<len(s)):
                    s[i+2]='O'
                ret+=1
                i+=2
            i+=1
        return ret
