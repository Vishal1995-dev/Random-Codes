class Solution(object):
    def countEven(self, num):
        """
        :type num: int
        :rtype: int
        """
        if(num>10):
            ret=4
            s=10
            while(s+10<num):
                s+=10
                ret+=5
            for i in range(s,num+1):
                su=0
                while(i):
                    su+=i%10
                    i//=10
                if(su%2==0):
                    ret+=1
            return ret
        else:
            ret=0
            for i in range(1,num+1):
                su=0
                while(i):
                    su+=i%10
                    i//=10
                if(su%2==0):
                    ret+=1
            return ret
        
