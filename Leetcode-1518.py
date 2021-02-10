class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        ret=numBottles
        while(numBottles>=numExchange):
            rem=numBottles
            ret+=rem/numExchange
            numBottles=(rem/numExchange)+(rem%numExchange)
        return ret
