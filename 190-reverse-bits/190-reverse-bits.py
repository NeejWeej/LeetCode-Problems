class Solution:
    def reverseBits(self, n: int) -> int:
        ans = n & 1
        digitsOfN = 1
        n >>= 1
        while n != 0:
            ans <<= 1
            bit = n & 1
            ans += bit
            n >>= 1
            digitsOfN += 1
        ans <<= 32 - digitsOfN
        return ans
        