class Solution(object):
    def strongPasswordCheckerII(self, password):
        """
        :type password: str
        :rtype: bool
        """
        special="!@#$%^&*()-+"
        if(len(password)<8):
            return False
        d={}
        d["lower"]=0
        d["upper"]=0
        d["digit"]=0
        d["special"]=0
        for i in range(len(password)):
            if(password[i].islower()):
                d["lower"]+=1
            if(password[i].isupper()):
                d["upper"]+=1
            if(password[i].isdigit()):
                d["digit"]+=1
            if(password[i] in special):
                d["special"]+=1
            if(i>0 and password[i]==password[i-1]):
                return False
        for i in d:
            if(d[i]==0):
                return False
        return True
