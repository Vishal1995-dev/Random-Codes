class Solution(object):
    def convertTime(self, current, correct):
        """
        :type current: str
        :type correct: str
        :rtype: int
        """
        a=int(current[:2])*60+int(current[3:])
        b=int(correct[:2])*60+int(correct[3:])
        ret=0
        ret+=abs(a-b)//60
        val=abs(a-b)%60
        ret+=val//15
        val=val%15
        ret+=val//5
        val=val%5
        ret+=val
        return ret
