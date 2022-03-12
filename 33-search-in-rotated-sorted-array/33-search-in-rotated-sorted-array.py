class Solution:
    def binSearch(nums, target):
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        if nums[start] == target:
            return start
        return -1
    
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        if nums[n - 1] >= nums[0]:
            return Solution.binSearch(nums, target)
    
        start = 0
        end = len(nums) - 1
        rot_idx = 0
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] > nums[mid + 1]:
                rot_idx = mid + 1
                break
            elif nums[mid] > nums[start]:
                start = mid + 1
            else:
                end = mid
        # print(rot_idx)
        if target == nums[rot_idx]:
            return rot_idx
        
        if target <= nums[n-1]:
            idx = Solution.binSearch(nums[rot_idx:], target)
            if idx == -1:
                return idx
            return idx + rot_idx
        else:
            idx = Solution.binSearch(nums[:rot_idx], target)
            return idx
        
        
        
                

        
            
                
        