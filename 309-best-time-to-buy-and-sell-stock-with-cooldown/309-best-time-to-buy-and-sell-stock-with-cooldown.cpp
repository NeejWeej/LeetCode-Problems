class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int bestCool = 0;
        int bestHold = -prices[0];
        int bestSell = INT_MIN;
        int oldSell = bestSell;
        
        for(auto p: prices){
            oldSell = bestSell;
            
            bestSell = max(bestSell, bestHold + p);
            
            bestHold = max(bestCool - p, bestHold);
            
            bestCool = max(bestCool, oldSell);
        }
        
        return max(bestSell, bestCool);
    }
};