class Solution {
public:
    string shiftingLetters(string S, vector<int>& shifts) {
        int l=shifts.size();
        S[l-1]=(S[l-1] - 'a' + shifts[l-1]) % 26 + 'a';
        for(int i=l-2;i>=0;i--)
        {
            shifts[i]=(shifts[i]+shifts[i+1])%26;
            S[i]=(S[i] - 'a' + shifts[i]) % 26 + 'a';
        }
        return S;
    }
};
