class Solution(object):
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        def check(n):
            d=[]
            while(n):
                d.append(n%10)
                n//=10
            for i in d:
                if(digits.count(i)<d.count(i)):
                    return False
            return True
        
        ret=[]
        for i in range(100,999,2):
            if check(i):
                ret.append(i)
        return ret
