import bisect
class Solution:            
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        new_list = []
        res = [0 for _ in range(n)]
        for i in range(n - 1, -1, -1):
            to_add = nums.pop()
            idx = bisect.bisect_left(new_list, to_add)
            res[i] = idx
            new_list.insert(idx, to_add)
        return res
                        
        