class Solution {
public:
    
    std::function<bool(int)> getBestFunc(int last){
        return [=](int cur) -> bool
    {
        return last < cur;
    };
        
    }
    
    // bool biggerLast(int cur, int last){
    //         return last < cur;
    // }
    
    int findMin(vector<int>& nums) {
        
        int left = 0;
        int right = nums.size();
        int last = nums.back();
        
        if (nums.front() <= last) return nums[0];
        
        auto biggerLast = getBestFunc(last);
            
        while (left < right){
            int mid = (left + right) / 2;
            
            if (biggerLast(nums[mid]))
                left = mid + 1;
            
            else right = mid;
        }
        
        return nums[left];
    }
};