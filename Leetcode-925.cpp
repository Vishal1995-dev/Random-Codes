class Solution {
public:
    bool isLongPressedName(string name, string typed) {
        int i=0;
        int j=0;
        while(i<name.size()) {
            int c=0;
            char s=name[i];
            if(typed[j]!=s) return false;
            while(i<name.size() && s==name[i]) {
                i++;
                c++;
            }
            int co=0;
            while(j<typed.size() && s==typed[j]) {
                co++;
                j++;
            }
            if(co<c) return false;
        }
        if(j!=typed.size()) return false;
        return true;
    }
};
