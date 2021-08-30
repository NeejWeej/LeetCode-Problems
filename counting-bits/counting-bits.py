class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n+1)
        ans[0] = 0
        big_pow_2 = 1
        for i in range(1, n+1):
            if i == big_pow_2 * 2:
                big_pow_2 = i
            ans[i] = ans[i-big_pow_2] + 1
        return ans
            
        