class Solution {
public:
    int minDominoRotations(vector<int>& tops, vector<int>& bottoms) {
        int ret=INT_MAX;
        for(int i=1;i<7;i++) {
            int ups=0,downs=0,up=0,down=0;
            for(int j=0;j<tops.size();j++) {
                if(tops[j]==i)
                    ups+=1;
                if(bottoms[j]==i)
                    downs+=1;
                if(tops[j]!=i and bottoms[j]==i)
                    up+=1;
                if(tops[j]==i and bottoms[j]!=i)
                    down+=1;
            }
            if(ups+up==downs+down and ups+up==tops.size()) {
                if(ret>up) ret=up;
                if(ret>down) ret=down;
            }
        }
        if(ret!=INT_MAX)
            return ret;
        return -1;
    }
};
