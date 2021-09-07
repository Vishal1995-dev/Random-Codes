class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret=0
        curr=1
        prev=0
        for i in range(1,len(s)):
            if(s[i]==s[i-1]):
                curr+=1
            else:
                ret+=min(curr,prev)
                prev=curr
                curr=1
        return ret+min(curr,prev)
