class Solution {
public:
    vector<vector<int>> ret;
    int n;
    
    void getPath(vector<vector<int>>& graph,int i,vector<int>path) {
        path.push_back(i);
        if(i==n-1) ret.push_back(path);
        else {
            for(int p:graph[i]) getPath(graph,p,path);
        }
        path.pop_back();
    }
    
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
        n=graph.size();
        getPath(graph,0,{});
        return ret;
        
    }
};
