class Solution(object):
    def largestInteger(self, num):
        """
        :type num: int
        :rtype: int
        """
        ret=0
        e=[]
        o=[]
        s=str(num)
        for i in s:
            if(int(i)%2==0):
                e.append(int(i))
            else:
                o.append(int(i))
        e.sort(reverse=True)
        o.sort(reverse=True)
        for i in s:
            if(int(i)%2==0):
                ret=ret*10+e.pop(0)
            else:
                ret=ret*10+o.pop(0)
        return ret
