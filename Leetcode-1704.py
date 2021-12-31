class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vowel="aeiouAEIOU"
        i=0
        j=len(s)-1
        cnt1=0
        cnt2=0
        while(i<j):
            if(s[i] in vowel):
                cnt1+=1
            if(s[j] in vowel):
                cnt2+=1
            i+=1
            j-=1
        return cnt1==cnt2
