class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        total = 0
        num_good_pairs = {}
        last_time_num_seen = {}
        dp = [0]*len(nums)
        for idx,val in enumerate(nums[::-1]):
            if val not in last_time_num_seen:
                last_time_num_seen[val] = idx
                dp[idx] = 0
                continue
            else:
                last = last_time_num_seen[val]
                dp[idx] = dp[last] + 1
                last_time_num_seen[val] = idx
            total += dp[idx]
        print(dp)
        # for val in nums[::-1]:
        #     if val in num_good_pairs:
        #         num_good_pairs[val] = 2*num_good_pairs.get(val) + 1
        #     else:
        #          num_good_pairs[val] = 0
        # for count in num_good_pairs.values():
        #     total += count
        return total
        