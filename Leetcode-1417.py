class Solution(object):
    def reformat(self, s):
        """
        :type s: str
        :rtype: str
        """
        ret=''
        c=[]
        n=[]
        for i in s:
            if(i.isdigit()):
                n.append(i)
            else:
                c.append(i)
        if(abs(len(c)-len(n))>1):
            return ""
        if(len(c)>len(n)):
            ret+=c[0]
            for i in range(len(n)):
                ret+=n[i]+c[i+1]
            return ret
        elif(len(c)<len(n)):
            ret+=n[0]
            for i in range(len(c)):
                ret+=c[i]+n[i+1]
            return ret
        else:
            for i in range(len(c)):
                ret+=c[i]+n[i]
            return ret
