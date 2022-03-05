class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        ret=0
        for i in range(len(tickets)):
            if(i<=k):
                if(tickets[i]>=tickets[k]):
                    ret+=tickets[k]
                else:
                    ret+=tickets[i]
            else:
                if(tickets[i]>=tickets[k]):
                    ret+=tickets[k]-1
                else:
                    ret+=tickets[i]
        return ret
