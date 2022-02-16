class Solution(object):
    def reformatNumber(self, number):
        """
        :type number: str
        :rtype: str
        """
        s=""
        for i in number:
            if(i!=" " and i!="-"):
                s+=i
        ret=""
        i=0
        l=len(s)
        while(i<l):
            if(l-i==4):
                ret+=s[i:i+2]+"-"
                i+=2
                ret+=s[i:i+2]+"-"
                break
            ret+=s[i:i+3]
            i+=3
            ret+="-"
        return ret[:-1]
