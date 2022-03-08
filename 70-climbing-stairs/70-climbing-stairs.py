class Matrix:
    def __init__(self, vals):
        self.a, self.b, self.c, self.d = vals[0], vals[1], vals[2], vals[3]
    
    def vec_mult(self, x, y):
        top = self.a * x + self.b * y
        bot = self.c * x + self.d * y
        return [top, bot]
    
    def mat_mult(self, mat):
        a = self.a * mat.a + self.b * mat.c
        b = self.a * mat.b + self.b * mat.d
        c = self.c * mat.a + self.d * mat.c
        d = self.c * mat.b + self.d * mat.d
        
        self.a, self.b, self.c, self.d = a, b, c, d
        return
        
        
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        two = 2
        one = 1
        
        cur_mat = Matrix([1, 0, 0, 1])
        pow_2_mat = Matrix([1, 1, 1, 0])
        
        n = n - 2
        while n > 0:
            if n % 2 == 1:
                cur_mat.mat_mult(pow_2_mat)
            pow_2_mat.mat_mult(pow_2_mat)
            n = n >> 1
        last_2 = cur_mat.vec_mult(two, one)
        return last_2[0]
        
        
            