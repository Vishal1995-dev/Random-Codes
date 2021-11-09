class Solution(object):
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """
        ret=[]
        l=sentence.split(" ")
        for i in range(len(l)):
            if(l[i][0]=='a' or l[i][0]=='e' or l[i][0]=='i' or l[i][0]=='o' or l[i][0]=='u' or l[i][0]=='A' or l[i][0]=='E' or l[i][0]=='I' or l[i][0]=='O' or l[i][0]=='U'):
                ele=l[i]
            else:
                ele=l[i][1:]+l[i][:1]
            ele+="ma"
            for j in range(i+1):
                ele+="a"
            ret.append(ele)
        return " ".join(ret)
            
                
