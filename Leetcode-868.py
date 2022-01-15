class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=[]
        while(n):
            a.append(n%2)
            n//=2
        ret=0
        i=0
        j=0
        while(j<len(a)):
            if(a[j]==1):
                i=j+1
                while(i<len(a) and a[i]!=1):
                    i+=1
                if(i<len(a) and a[i]==1):
                    ret=max(ret,(i-j))
            j+=1
        return ret
