class Solution(object):
    def arrangeWords(self, text):
        """
        :type text: str
        :rtype: str
        """
        text=text.lower()
        a=text.split(" ")
        a.sort(key=len)
        s=''
        s+=a[0][0].upper()
        s+=a[0][1:]
        a[0]=s
        return ' '.join(a)
