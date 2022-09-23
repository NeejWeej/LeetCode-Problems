class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_map<int, int> seen;
        
        for(int i = 0; i < nums.size(); ++i){
            int num = nums[i];
            auto val = seen.find(num);
            if (val != seen.end()){
                // cout<< num<< "\n";
                // cout<< i << " "<< val->second << " "<< k << "\n";
                if (i - (val->second) <= k) return true;
            }            
            seen[num] = i;
        }
        for(auto& m : seen){
            cout<< m.first << " " << m.second << "\n";
        }
        return false;        
    }
};