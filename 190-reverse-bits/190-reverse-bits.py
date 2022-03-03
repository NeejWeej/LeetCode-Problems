class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        
        for _ in range(32):
            if n % 2 == 0:
                ans = ans << 1
            elif n % 2 == 1:
                ans = ans << 1
                ans += 1
            n = n >> 1
        return ans