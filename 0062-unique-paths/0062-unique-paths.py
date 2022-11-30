class Solution:
    def fallingFact(self, n, r):
        ans = 1
        for i in range(r):
            ans *= n
            n -= 1
        return ans
    
    def nCr(self, n, r):
        return self.fallingFact(n, r) // self.fallingFact(r, r)
    
    def uniquePaths(self, m: int, n: int) -> int:
        return self.nCr(m + n - 2, m - 1)