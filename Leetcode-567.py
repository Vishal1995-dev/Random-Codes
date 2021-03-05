class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        n=len(s1)
        s1_l=list(s1)
        s1_l.sort()
        for i in range(len(s2)-n+1):
            s_new=s2[i:i+n]
            s_new_l=list(s_new)
            s_new_l.sort()
            if(s_new_l==s1_l):
                return True
        return False
