class Solution(object):
    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """
        ret=[]
        i=0
        j=1
        while((j)<=label):
            i+=1
            j*=2
        while(label!=0):
            ret.append(label)
            l1=2**i-1
            l0=2**(i-1)
            label=(l1+l0-label)//2
            i-=1
        return ret[::-1]
