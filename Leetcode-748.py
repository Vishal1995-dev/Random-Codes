class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        a={}
        licensePlate=licensePlate.lower()
        for i in licensePlate:
            if(i.isalpha()):
                if(ord(i) in a):
                    a[ord(i)]+=1
                else:
                    a[ord(i)]=1

        words=sorted(words,key=len)
        for i in words:
            flag=0
            for j in a:
                if(i.count(chr(j))<a[j]):
                    flag=1
                    break
            if(flag==0):
                return i
