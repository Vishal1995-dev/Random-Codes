class Solution(object):
    def bestHand(self, ranks, suits):
        """
        :type ranks: List[int]
        :type suits: List[str]
        :rtype: str
        """
        three=0
        pair=0
        d={}
        for i in ranks:
            if(i in d):
                d[i]+=1
            else:
                d[i]=1
            if(d[i]==3):
                three=1
            if(d[i]==2):
                pair+=1
        if(len(set(suits))==1):
            return "Flush"
        elif(three):
            return "Three of a Kind"
        elif(pair):
            return "Pair"
        else:
            return "High Card"
