class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        def check(l,i):
            if(i==len(s)):
                ret.append(" ".join(l))
            for j in range(i+1,len(s)+1):
                if(s[i:j] in wordDict):
                    check(l+[s[i:j]],j)
        
        ret=[]
        check([],0)
        return ret
