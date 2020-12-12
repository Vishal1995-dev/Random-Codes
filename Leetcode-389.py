class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        a={}
        for i in s:
            if(i in a):
                a[i]+=1
            else:
                a[i]=1
        for i in t:
            if(i in a):
                if(a[i]==0):
                    return i
                a[i]-=1
            else:
                return i
