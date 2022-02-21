class Solution:
    import collections
    def subarraySum(self, nums: List[int], k: int) -> int:
        running_tot = 0
        prefix_sum = []
        ans = 0
        for num in nums:
            running_tot += num
            prefix_sum.append(running_tot)
            if running_tot == k:
                ans += 1
        prefix_sum_set = Counter(prefix_sum)
        for cur_sum in prefix_sum:
            cur_count = prefix_sum_set.get(cur_sum)
            if cur_count == 1:
                del prefix_sum_set[cur_sum]
            else:
                prefix_sum_set[cur_sum] = cur_count - 1
            if k + cur_sum in prefix_sum_set:
                ans += prefix_sum_set.get(k + cur_sum)
        return ans
        
        