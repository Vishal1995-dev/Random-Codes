class Solution(object):
    def maximumPopulation(self, logs):
        """
        :type logs: List[List[int]]
        :rtype: int
        """
        a=[0]*(100+1)
        for i in logs:
            a[i[0]-1950]+=1
            a[i[1]-1950]-=1
    
        m=a[0]
        ind=0
        for i in range(1,100):
            a[i]+=a[i-1]
            if(a[i]>m):
                m=a[i]
                ind=i
            
        return ind+1950
            
