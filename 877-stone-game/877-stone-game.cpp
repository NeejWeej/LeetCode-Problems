class Solution {
public:
    bool stoneGame(vector<int>& piles) {
        int n = piles.size();
        vector<vector<int>> dp(n, vector<int>(n, 0));
        for(int i = 0; i < n; ++ i){
            dp[i][i] = piles[i];
        }
        
        for(int len = 2; len <= n; ++len){
            for(int s = 0; s <= n - len; ++s){
                int e = s + len - 1;
                int takeStart = piles[s] - dp[s + 1][e];
                int takeEnd = piles[e] - dp[s][e - 1];
                dp[s][e] = max(takeStart, takeEnd);
            }
            
        }
        return dp[0][n-1] > 0;
    }
};