class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int, int> seen;
        
        for(int num: nums){
            if(seen.find(num) != seen.end()) return true;
            seen.insert({num, 1});
        }
        return false;
        
    }
};