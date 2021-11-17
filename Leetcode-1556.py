class Solution(object):
    def thousandSeparator(self, n):
        """
        :type n: int
        :rtype: str
        """
        s=""
        l=list(str(n))
        n=len(l)
        i=n-1
        while(i>=0):
            j=0
            while(i-j>=0 and j<3):
                s+=l[i-j]
                j+=1
            i-=3
            s+="."
        s=s[::-1]
        return s[1:]
