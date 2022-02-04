class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret=0
        for i in nums:
            cnt=0
            while(i):
                i//=10
                cnt+=1
            if(cnt%2==0):
                ret+=1
        return ret
