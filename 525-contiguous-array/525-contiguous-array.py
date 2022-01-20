class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        counts = {0:-1}
        count = 0
        best_len = 0
        for idx, val in enumerate(nums):
            if val == 1:
                count += 1
            else:
                count -= 1
            if count not in counts:
                counts[count] = idx
            else:
                best_len = max(best_len, idx - counts.get(count))
        return best_len
                