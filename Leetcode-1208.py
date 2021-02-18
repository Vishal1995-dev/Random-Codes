class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        a=[]
        for i in range(len(s)):
            a.append(abs(ord(s[i])-ord(t[i])))
        a.sort()
        print(a)
        su=0
        ret=-1
        i=0
        while(su<=maxCost):
            su+=a[i]
            i+=1
            ret+=1
        return ret
