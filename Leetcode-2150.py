class Solution(object):
    def findLonely(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        c=defaultdict(int)
        for i in nums:
            c[i]+=1
        ret=[]
        for i in c:
            if(c[i]==1 and i+1 not in c and i-1 not in c):
                ret.append(i)
        return ret
