class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        i=0
        l=len(s)
        ret=""
        while(i<l):
            if(i+2<l and s[i+2]=='#'):
                ret+=chr(ord('a')+int(s[i:i+2])-1)
                i+=2
            else:
                ret+=chr(ord('a')+int(s[i])-1)
            i+=1
        return ret
