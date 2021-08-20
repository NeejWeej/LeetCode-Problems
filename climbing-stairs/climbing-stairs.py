class Solution:
    def climbStairs(self, n: int) -> int:
        x = 1
        y = 0
        for i in range(n):
            temp = x + y
            y = x
            x = temp
        return x