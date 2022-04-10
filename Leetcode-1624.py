class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        st={}
        e={}
        i=0
        j=len(s)-1
        while(i<len(s)):
            if(s[i] not in st):
                st[s[i]]=i
            if(s[j] not in e):
                e[s[j]]=j
            i+=1
            j-=1
        ret=-1
        for i in st:
            if(st[i]!=e[i]):
                ret=max(ret,e[i]-st[i]-1)
        return ret
