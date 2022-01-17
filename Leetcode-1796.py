class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        digit=set()
        for i in s:
            if(i.isdigit()):
                digit.add(i)
        digit=list(digit)
        digit.sort(reverse=True)
        if(len(digit)<2):
            return -1
        else:
            return digit[1]
