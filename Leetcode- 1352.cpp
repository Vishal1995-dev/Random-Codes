class ProductOfNumbers {
public:
    vector<long long> a = {1};
    
    ProductOfNumbers() {
    }
    
    void add(int num) {
        if(num==0) a={1};
        else a.push_back(a.back()*num);
    }
    
    int getProduct(int k) {
        if(k>=a.size()) return 0;
        return a.back()/a[a.size()-k-1];
    }
};

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * ProductOfNumbers* obj = new ProductOfNumbers();
 * obj->add(num);
 * int param_2 = obj->getProduct(k);
 */
