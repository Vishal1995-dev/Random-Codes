class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        a=[]
        while(num):
            a.append(int(num%10))
            num//=10
        a.sort()
        return a[0]*10+a[3]+a[1]*10+a[2]
    
