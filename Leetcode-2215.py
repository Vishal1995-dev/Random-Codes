class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        l={}
        l2=set()
        for i in nums1:
            l[i]=1
        for i in nums2:
            if(i in l):
                l[i]+=2
            else:
                l2.add(i)
        l1=[]
        for i in l:
            if(l[i]==1):
                l1.append(i)
        return [l1,list(l2)]
