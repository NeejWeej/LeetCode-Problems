class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        A = nums1
        B = nums2
        dp = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]
        best = [0,0,0]
        for i in range(1, len(A) + 1):
            for j in range(1, len(B) + 1):
                if A[i - 1] == B[j - 1]:
                    new_val = dp[i - 1][j - 1] + 1
                    dp[i][j] = new_val
                    if new_val > best[0]:
                        best = [new_val, i - new_val, i-1]
        print(A[best[1]: best[2] + 1])
        return best[0]            
        # return max(max(row) for row in dp)