class Solution(object):
    def buddyStrings(self, s, g):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if(len(s)!=len(g)):
            return False
        v=0
        a=[]
        d={}
        flag=0
        for i in range(len(s)):
            if(s[i] in d):
                d[s[i]]+=1
            else:
                d[s[i]]=1
            if(d[s[i]]>1):
                flag=1
            if(s[i]!=g[i]):
                v+=1
                a.append([s[i],g[i]])
            if(v>2):
                return False
        if(v==0):
            return flag==1
        if(len(a)<2):
            return False
        return a[0][1]==a[1][0] and a[1][1]==a[0][0]
