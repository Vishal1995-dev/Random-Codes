class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        ret=[]
        l=len(s)
        i=0
        while(i<l):
            val=k
            st=""
            while(val>0 and i<l):
                st+=s[i]
                val-=1
                i+=1
                if(i==l and val>0):
                    while(val>0):
                        st+=fill
                        val-=1
            ret.append(st)
        return ret
