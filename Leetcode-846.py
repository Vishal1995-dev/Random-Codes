class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        if(len(hand)%W!=0):
            return False
        
        hand.sort()

        while(len(hand)!=0):
            i=1
            p=hand[0]
            hand.remove(p)
            i+=1
            while(i<=W):
                if(p+1 in hand):
                    hand.remove(p+1)
                else:
                    return False
                i+=1
                p+=1
        return True
