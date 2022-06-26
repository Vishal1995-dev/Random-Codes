class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        ret=[]
        d={}
        for i in nums1:
            if(i not in d):
                d[i]=1
        for i in nums2:
            if(i in d):
                if(d[i]==1):
                    ret.append(i)
                    d[i]=0
            else:
                d[i]=2
        for i in nums3:
            if(i in d):
                if(d[i]==1 or d[i]==2):
                    ret.append(i)
                    d[i]=0
        return ret
