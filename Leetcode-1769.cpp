class Solution {
public:
    vector<int> minOperations(string boxes) {
        vector<int>ret(boxes.length());
        for(int i=1,l=0,l_c=0;i<boxes.length();i++) {
            if(boxes[i-1]=='1') l+=1;
            l_c+=l;
            ret[i]=l_c;
        }
        for(int i=boxes.length()-2,l=0,l_c=0;i>=0;i--) {
            if(boxes[i+1]=='1') l+=1;
            l_c+=l;
            ret[i]+=l_c;
        }
        return ret;
    }
};
