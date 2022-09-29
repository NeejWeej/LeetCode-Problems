class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> seen;
        
        for(auto num: nums){
            seen.insert(num);
        }
        
        int best = 0;
        
        for (auto num: nums){
            if(!seen.count(num - 1)){
                int cur = 0;
                while (seen.count(num)){
                    ++num;
                    ++cur;
                }
                best = max(best, cur);
            }
        }
        return best;
        
        
    }
};