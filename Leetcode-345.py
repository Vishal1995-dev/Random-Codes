class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel="aeiouAEIOU"
        l=len(s)
        a=[' ']*l
        i=0
        l-=1
        while(i<=l):
            if(s[i] in vowel and s[l] in vowel):
                a[i]=s[l]
                a[l]=s[i]
                i+=1
                l-=1
            else:
                if(s[i] not in vowel):
                    a[i]=s[i]
                    i+=1
                if(s[l] not in vowel):
                    a[l]=s[l]
                    l-=1
        return "".join(a)
