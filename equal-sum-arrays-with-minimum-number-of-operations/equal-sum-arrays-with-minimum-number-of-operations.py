class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        #BFS search
        n1 = sum(nums1)
        n2 = sum(nums2)
        
        if n1 == n2:
            return 0
        
        big, big_sum = nums1, n1
        small, small_sum = nums2, n2
        if n1 < n2:
            big, big_sum, small, small_sum = small, small_sum, big, big_sum
        
        big.sort()
        small.sort(reverse = True)
        ans = 0
        cur_dif = big_sum - small_sum
        while True:
            if cur_dif == 0:
                return ans
            if not big and not small:
                return -1
            
            elif big and not small:
                big_num = big[-1]
                ans += 1
                if cur_dif < big_num - 1:
                    return ans
                cur_dif -= big_num - 1
                big.pop()
                
            elif small and not big:
                small_num = small[-1]
                ans += 1
                if cur_dif < 6 - small_num:
                    return ans
                cur_dif -= 6 - small_num
            
            elif small and big:
                big_num = big[-1]
                small_num = small[-1]
                if big_num - 1 > 6 - small_num:
                    ans += 1
                    if cur_dif < big_num - 1:
                        return ans
                    cur_dif -= big_num - 1
                    big.pop() 
                else:
                    ans += 1
                    if cur_dif < 6 - small_num:
                        return ans
                    cur_dif -= 6 - small_num
                    small.pop()
            
            
#         count_big = {i:0 for i in range(1, 7)}
#         count_small = {i:0 for i in range(1, 7)}
#         for num in big:
#             count_big[num] += 1
#         for num in small:
#             count_small[num] += 1
        
#         while small_sum < big_sum:
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         sum1, sum2 = sum(nums1), sum(nums2)
#         diff = abs(sum1 - sum2)
#         count = 0
#         if diff == 0:
#             return count
#         l, s = nums2, nums1
#         if sum1 > sum2:
#             l = nums1
#             s = nums2
#         biggest_diff_l = [num - 1 for num in l]
#         biggest_diff_s = [6 - num for num in s]
#         total = biggest_diff_l + biggest_diff_s
#         total.sort(reverse = True)
#         for change in total:
#             diff -= change
#             count += 1
#             if diff <= 0:
#                 return count
#         return -1
        
        