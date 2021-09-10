class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        ret=0
        for i in range(len(s)):
            d={}
            j=i
            max_unique=0
            greater_k=0
            while(j<len(s)):
                if(s[j] in d):
                    d[s[j]]+=1
                else:
                    max_unique+=1
                    d[s[j]]=1
                if(d[s[j]]==k):
                    greater_k+=1
                if(max_unique==greater_k):
                    ret=max(ret,(j-i+1))
                j+=1
        return ret
