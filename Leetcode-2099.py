class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        a=[]
        j=0
        for i in nums:
            a.append((i,j))
            j+=1
        a.sort(reverse=True)
        b=[]
        for i in range(k):
            b.append((a[i][1],a[i][0]))
        b.sort()
        ret=[]
        for i in b:
            ret.append(i[1])
        return ret
