class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        d={'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        
        ret=[]
        
        if(len(digits)==0):
            return ret
        
        if(len(digits)==1):
            return d[digits[0]]
        
        def combine(s,left):
            if(len(left)==0):
                ret.append(s)
            else:
                for l in d[left[0]]:
                    combine(s+l,left[1:])
        
        combine("",digits)
        return ret    
        
