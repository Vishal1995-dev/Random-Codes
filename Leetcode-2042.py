class Solution(object):
    def areNumbersAscending(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i=0
        l=len(s)
        ret=-1
        while(i<l):
            if(s[i].isdigit()):
                r=""
                while(i<l and s[i].isdigit()):
                    r+=s[i]
                    i+=1
                if(int(r)<=ret):
                    return False
                ret=int(r)
            else:
                i+=1
        return True
