class RandomizedSet {
    vector<int>v;
    map<int,int>m;
public:
    /** Initialize your data structure here. */
    RandomizedSet() {
            
    }
    
    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    bool insert(int val) {
        if(m[val]==1) return false;
        m[val]=1;
        v.push_back(val);
        return true;
    }
    
    /** Removes a value from the set. Returns true if the set contained the specified element. */
    bool remove(int val) {
        if(m[val]==0) return false;
        m[val]=0;
        return true;
    }
    
    /** Get a random element from the set. */
    int getRandom() {
        while(true) {
            int r = rand() % v.size();
            if(m[v[r]]==1)
                return v[r];
        }
        return 0;
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */
