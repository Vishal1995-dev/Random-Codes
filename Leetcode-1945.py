class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        def convert(v,k):
            while(k>0):
                ret=0
                while(v):
                    ret+=v%10
                    v//=10
                v=ret
                k-=1
            return v
            
        s_new=""
        for i in s:
            s_new+=str(ord(i)-ord('a')+1)
        return convert(int(s_new),k)
            
