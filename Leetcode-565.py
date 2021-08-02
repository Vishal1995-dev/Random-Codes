class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret=0
        r=[1]*len(nums)
        
        def track(i):
            s=1
            r[i]=0
            j=nums[i]
            r[j]=0
            while(nums[j]!=i):
                j=nums[j]
                r[j]=0
                s+=1
            return s
            
        for i in range(len(nums)):
            if(r[i]!=0):
                if(nums[i]==i):
                    ret=max(ret,1)
                else:
                    ret=max(ret,track(i)+1)
        
        return ret
