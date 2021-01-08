class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s1=''
        a={}
        c=0
        for i in s:
            if(i not in a):
                a[i]=c
                c+=1
            s1+=str(a[i])
        s2=''
        a={}
        c=0
        for i in t:
            if(i not in a):
                a[i]=c
                c+=1
            s2+=str(a[i])
        return s1==s2
