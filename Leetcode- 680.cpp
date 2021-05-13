class Solution {
public:
    bool check(string s,int start,int end,int count)
    {
        while(start<end) {
            if(s[start]==s[end]) {
                start++;
                end--;
            }
            else if(count==1) return check(s,start+1,end,0) || check(s,start,end-1,0);
            else return false;
        }
        return true;
    }
    bool validPalindrome(string s) {
        return check(s,0,s.length()-1,1);
    }
};
