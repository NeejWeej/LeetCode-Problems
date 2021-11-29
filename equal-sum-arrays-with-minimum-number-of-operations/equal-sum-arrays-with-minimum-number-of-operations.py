class Solution:
    def drop(self, dif, count_big, count_small):
        ans = 0
        for i in range(5, 0, -1):
            drop = i *(count_big[i + 1] + count_small[6 - i])
            if dif <= drop:
                to_add = math.ceil(dif/i)
                return ans + to_add
            dif -= drop
            ans += (count_big[i + 1] + count_small[6 - i])
        if dif > 0:
            return -1
        
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = sum(nums1)
        n2 = sum(nums2)   
        if n1 == n2:
            return 0
        
        big, big_sum = nums1, n1
        small, small_sum = nums2, n2
        if n1 < n2:
            big, big_sum, small, small_sum = small, small_sum, big, big_sum
            
        count_big = {i:0 for i in range(6, 0, -1)}
        count_small = {i:0 for i in range(1, 7)}
        for num in big:
            count_big[num] += 1
        for num in small:
            count_small[num] += 1
        cur_dif = big_sum - small_sum

        return self.drop(cur_dif, count_big, count_small)
            
        
#         five_drop = 5 *(count_big[6] + count_small[1])
#         if cur_dif < five_drop:
#             return math.ceil(cur_dif/5)
#         cur_dif -= five_drop
        
#         while True:
#             if cur_dif == 0:
#                 return ans
            
#             if len(count_big) == 0 and len(count_small) == 0:
#                 return -1
                
#             elif len(count_big) > 0 and len(count_small) == 0:
#                 big_num = next(iter(count_big))
#                 if count_big.get(big_num) <= 0:
#                     del count_big[big_num]
#                     continue
#                 ans += 1
#                 if cur_dif <= big_num - 1:
#                     return ans
#                 cur_dif -= big_num - 1
#                 count_big[big_num] -= 1
#                 if count_big.get(big_num) <= 0:
#                     del count_big[big_num]
                
#             elif len(count_big) == 0 and len(count_small) > 0:
#                 small_num = next(iter(count_small))
#                 if count_small.get(small_num) <= 0:
#                     del count_small[small_num]
#                     continue
#                 ans += 1
#                 if cur_dif <= 6 - small_num:
#                     return ans
#                 cur_dif -= 6 - small_num
#                 count_small[small_num] -= 1
#                 if count_small.get(small_num) <= 0:
#                     del count_small[small_num]
            
#             elif len(count_big) > 0 and len(count_small) > 0:
#                 big_num = next(iter(count_big))
#                 small_num = next(iter(count_small))
#                 if count_big.get(big_num) <= 0:
#                     del count_big[big_num]
#                     continue
#                 if count_small.get(small_num) <= 0:
#                     del count_small[small_num]
#                     continue
#                 if big_num - 1 > 6 - small_num:
#                     ans += 1
#                     if cur_dif <= big_num - 1:
#                         return ans
#                     cur_dif -= big_num - 1
#                     count_big[big_num] -= 1
#                     if count_big.get(big_num) <= 0:
#                         del count_big[big_num]
#                 else:
#                     ans += 1
#                     if cur_dif <= 6 - small_num:
#                         return ans
#                     cur_dif -= 6 - small_num
#                     count_small[small_num] -= 1
#                     if count_small.get(small_num) <= 0:
#                         del count_small[small_num]
        