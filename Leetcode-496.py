class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ret=[]
        d={}
        for i in range(len(nums2)):
            j=i+1
            while(j<len(nums2) and nums2[j]<nums2[i]):
                j+=1
            if(j==len(nums2)):
                d[nums2[i]]=-1
            else:
                d[nums2[i]]=nums2[j]
        for i in nums1:
            if(i in d):
                ret.append(d[i])
            else:
                ret.append(-1)
        return ret
