class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones.sort()
        while(len(stones)>1):
            stones.sort()
            n=len(stones)
            a=stones[n-1]
            b=stones[n-2]
            if(a==b):
                stones.pop()
                stones.pop()
            else:
                stones.pop()
                stones.pop()
                stones.append(abs(a-b))
        if(len(stones)!=0):
            return stones[0]
        return 0
