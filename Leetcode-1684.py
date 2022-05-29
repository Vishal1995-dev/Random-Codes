class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        ret=0
        a={}
        for i in allowed:
            a[i]=1
        for w in words:
            flag=0
            for c in w:
                if(c not in a):
                    flag=1
                    break
            if(flag==0):
                ret+=1
        return ret
