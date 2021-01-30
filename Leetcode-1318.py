class Solution(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        a_bin=bin(a).replace("0b", "")
        b_bin=bin(b).replace("0b", "")
        c_bin=bin(c).replace("0b", "")
        
        a_bin=a_bin[::-1]
        b_bin=b_bin[::-1]
        c_bin=c_bin[::-1]
        
        l=max(len(a_bin),len(b_bin),len(c_bin))
        
        if(l!=len(a_bin)):
            for i in range(len(a_bin),l):
                a_bin+='0'
        if(l!=len(b_bin)):
            for i in range(len(b_bin),l):
                b_bin+='0'
        if(l!=len(c_bin)):
            for i in range(len(c_bin),l):
                c_bin+='0'
        
        ret=0
        for i in range(l):
            if((a_bin[i]=='1' or b_bin[i]=='1') and c_bin[i]=='1'):
                continue
            elif((a_bin[i]=='1' and b_bin[i]=='1') and c_bin[i]!='1'):
                ret+=2
            elif(int(a_bin[i])+int(b_bin[i])!=int(c_bin[i])):
                ret+=1
        return ret
