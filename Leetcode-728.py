class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def check(i):
            val=i
            while(i):
                rem=i%10
                if(rem==0 or val%rem!=0):
                    return False
                i//=10
            return True
        
        ret=[]
        for i in range(left,right+1):
            if(check(i)):
                ret.append(i)
        return ret
