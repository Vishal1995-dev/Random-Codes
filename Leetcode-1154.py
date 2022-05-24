class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        mon=[31,28,31,30,31,30,31,31,30,31,30,31]
        y=int(date[:4])
        if((y%400==0 and y%100==0) or (y%4==0 and y%100!=0)):
            mon[1]+=1
        ret=0
        i=0
        m=int(date[5:7])
        while(i<m-1):
            ret+=mon[i]
            i+=1
        ret+=int(date[8:])
        return ret
