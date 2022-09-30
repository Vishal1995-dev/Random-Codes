class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        arr=[]
        for i in logs:
            if(i[0]=='.'):
                if(i[1]=='.' and len(arr)!=0):
                    arr.pop()
            else:
                arr.append(i[:-1])
        return len(arr)
