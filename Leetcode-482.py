class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s=s.replace("-","").upper()[::-1]
        ret=[]
        for i in range(0,len(s),k):
            ret.append(s[i:i+k])
        return "-".join(ret)[::-1]
