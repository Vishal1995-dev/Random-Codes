class Solution(object):
    def finalValueAfterOperations(self, o):
        """
        :type operations: List[str]
        :rtype: int
        """
        ret=0
        for i in o:
            if(i[0]=='+' or i[-1]=='+'):
                ret+=1
            else:
                ret-=1
        return ret
