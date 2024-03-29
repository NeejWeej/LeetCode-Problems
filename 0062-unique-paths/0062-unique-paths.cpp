
class Solution {
public:
    void addPrime(vector<int>& primes, const int val){
        for(auto p: primes){
            if (val % p == 0) return;
        }
        primes.push_back(val);
    }
    
    
    vector<int> primeList(const int v){
        vector<int> ans;
        ans.push_back(2);
        ans.push_back(3);
        
        for(int i = 6; i <= v + 1; i += 6 ){
            int less = i - 1;
            addPrime(ans, less);
            int greater = i + 1;
            addPrime(ans, greater); 
        }
        return ans;
        
    }
    
    unordered_map<int, int> fallingFact(int val, const int descent){
        unordered_map<int, int> ans;
        vector<int> primes = primeList(val);
        for(int i = 0; i < descent; i++){
            int temp = val;
            for(const auto& p: primes){
                if (temp < p) break;
                while (true){
                    auto dv = div(temp, p);
                    if (dv.rem == 0){
                        ans[p]++;
                        temp = dv.quot;
                    }
                    else break;
                }
            }
            val--;
        }
        return ans;
    }
    
    int nCr(const int n, const int r){
        unordered_map<int,int> num = fallingFact(n, r);
        unordered_map<int,int> denom = fallingFact(r, r);
        int ans = 1;
        
        for(const auto& [k,v]: denom) num[k] -= v;
        
        for(const auto& [k,v]: num) ans *= pow(k, v);
        
        return ans;
    }
    
    
    int uniquePaths(int m, int n) {
        if (m > n) swap(m,n);
        return nCr(m + n - 2, m - 1);
    }
};