class Solution {
public:
    
    // template<n>
    // static bool smallerLast(int cur){
    //     return cur <= n;
    // }
    bool biggerLast(int cur, int last){
            return last < cur;
    }
    
    int findMin(vector<int>& nums) {
        
        int left = 0;
        int right = nums.size();
        int last = nums.back();
        
        if (nums.front() <= last) return nums[0];
            
        while (left < right){
            int mid = (left + right) / 2;
            
            if (biggerLast(nums[mid], last))
                left = mid + 1;
            
            else right = mid;
        }
        
        return nums[left];
    }
};