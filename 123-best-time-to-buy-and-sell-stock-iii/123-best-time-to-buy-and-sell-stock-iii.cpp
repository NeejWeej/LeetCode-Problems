class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int bestBuy1 = INT_MIN;
        int bestSell1 = 0;
        int bestBuy2 = INT_MIN;
        int bestSell2 = 0;
        
        for(auto p: prices){
            bestBuy1 = max(-p, bestBuy1);
            bestSell1 = max(bestSell1, bestBuy1 + p);
            
            bestBuy2 = max(bestSell1 - p, bestBuy2);
            bestSell2 = max(bestSell2, bestBuy2 + p);
        }
        
        return bestSell2;
    }
};