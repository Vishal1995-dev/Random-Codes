class Solution(object):
    def digitCount(self, num):
        """
        :type num: str
        :rtype: bool
        """
        d=defaultdict(int)
        for i in num:
            d[int(i)]+=1
        for i in range(len(num)):
            if(d[i]!=int(num[i])):
                return False
        return True
