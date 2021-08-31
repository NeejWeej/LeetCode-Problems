class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        #BFS search
        sum1, sum2 = sum(nums1), sum(nums2)
        diff = abs(sum1 - sum2)
        count = 0
        if diff == 0:
            return count
        l, s = nums2, nums1
        if sum1 > sum2:
            l = nums1
            s = nums2
        biggest_diff_l = [num - 1 for num in l]
        biggest_diff_s = [6 - num for num in s]
        total = biggest_diff_l + biggest_diff_s
        total.sort(reverse = True)
        for change in total:
            diff -= change
            count += 1
            if diff <= 0:
                return count
        return -1
        
        