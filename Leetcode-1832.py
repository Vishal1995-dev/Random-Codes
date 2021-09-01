class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        if(len(sentence)<26):
            return False
        d={}
        for i in sentence:
            if(i in d):
                d[i]+=1
            else:
                d[i]=1
        return (len(d)==26)
