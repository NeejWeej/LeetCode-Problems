class Solution {
public:
    static bool sortEndTime(tuple<int,int,int>&a, tuple<int,int,int>& b){
        return get<1>(a) < get<1>(b);
    }
    
    static bool findFirstConflict(int s, const pair<int,int>& a){
        return s < get<0>(a);
    }
    
    int jobScheduling(vector<int>& startTime, vector<int>& endTime, vector<int>& profit) {
        int n = startTime.size();
        int ans = 0;
        
        vector<tuple<int,int,int>> pairs(n);
        for(int i = 0; i < n; ++i){
            pairs[i] = make_tuple(startTime[i], endTime[i], profit[i]);
        }
        
        sort(pairs.begin(), pairs.end(), Solution::sortEndTime);
        
        // dp stores (end, profit);
        
        vector<pair<int,int>> dp(n + 1);
        dp[0] = make_pair(INT_MIN, 0);
        
        for(int i = 0; i < n; ++i){
            auto& [s, e, p] = pairs[i];
            typedef vector<pair<int,int>> vecP;
            vecP::iterator last = ( dp.begin() + i + 1 );
            auto it = upper_bound(dp.begin(), last, s, Solution::findFirstConflict);
            if(it == last){
                dp[i + 1] = make_pair(e, dp[i].second + p);
            }
            else{
                --it;
                int profitWith = (*it).second + p;
                int profitWithout = dp[i].second; 
                dp[i+1] = (profitWith <= profitWithout)?dp[i]:make_pair(e, profitWith);
            }
        }
        return get<1>(dp.back());
    }
};