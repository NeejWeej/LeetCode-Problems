class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        for idx, num in enumerate(nums):
            if idx - seen.get(num, float('-inf')) <= k:
                return True
            seen[num] = idx
        return False
        