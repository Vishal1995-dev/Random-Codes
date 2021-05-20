class Solution {
public:
    int firstUniqChar(string s) {
        map<char,int> element;
        
        for(auto i:s){
            element[i]++;   
        }
        
        for(int i=0;i<=s.length()-1;i++) {
            if(element[s[i]]==1) return i;
        }
        
        return -1;
    }
};
