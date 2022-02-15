class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ret=[]
        for i in range(len(words)):
            for j in range(len(words)):
                if(i!=j):
                    if(words[i] in words[j]):
                        ret.append(words[i])
                        break
        return ret
