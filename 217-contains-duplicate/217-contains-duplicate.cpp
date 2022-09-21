class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int, int> seen;
        
        for(int num: nums){
            if(seen.count(num)) return true;
            seen.insert({num, 1});
        }
        return false;
        
    }
};