class Solution(object):
    def digitSum(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        def fun(st):
            if(len(st)<=k):
                return st
            s_ret=""
            for i in range(0,len(st),k):
                ret=0
                for j in range(i,min(i+k,len(st))):
                    ret+=ord(st[j])-ord('0')
                s_ret+=str(ret)
            return fun(s_ret)
                
        return fun(s)
