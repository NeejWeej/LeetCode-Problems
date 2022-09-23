class Solution {
public:
    
    static bool smallestDist(vector<int>& i1, vector<int>& i2){
        return i1.back() - i1.front() < i2.back() - i2.front();
    }
    
    vector<int> minInterval(vector<vector<int>>& intervals, vector<int>& queries) {
        int i = 0;
        
        set<int> sortedQueries;
        
        for(auto q: queries) sortedQueries.insert(q);
        
        sort(intervals.begin(), intervals.end(), Solution::smallestDist);
        size_t n = queries.size();
        
        
        vector<int> ans(n, -1);
        unordered_map<int, int> queryMap;
        
        for(auto v: intervals){
            int s = v.front(), e=v.back();
            auto it = sortedQueries.lower_bound(s);
            int size = e - s + 1;
            
            while(it != sortedQueries.end() && (*it) <= e){
                queryMap.insert({*it, size});
                it = sortedQueries.erase(it);
            }
        }
        
        for(int i = 0; i < queries.size(); ++i){
            int q = queries[i];
            auto itEle = queryMap.find(q);
            if(itEle != queryMap.end()) ans[i] = itEle->second;
        }
        
        return ans;
    }
};