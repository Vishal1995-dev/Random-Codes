class Solution(object):
    def isPrefixString(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: bool
        """
        l=len(s)
        st=""
        for i in words:
            st+=i
            if(len(st)==l and st==s):
                return True
            if(len(st)>l):
                return False
        return False
