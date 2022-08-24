class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        digitsOfN = 0
        while n != 0:
            ans <<= 1
            bit = n & 1
            ans += bit
            n >>= 1
            digitsOfN += 1
        ans <<= 32 - digitsOfN
        return ans
        