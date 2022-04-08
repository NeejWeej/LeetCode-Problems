class Matrix:
    def __init__(self, vals):
        self.vals = {i:x for i,x in enumerate(vals)}
    
    def vec_mult(self, x, y, z):
        top = self.vals[0] * x + self.vals[1] * y + self.vals[2] * z
        mid = self.vals[3] * x + self.vals[4] * y + self.vals[5] * z
        bot = self.vals[6] * x + self.vals[7] * y + self.vals[8] * z
        return [top, bot]
    
    def __matmul__(self, mat):
        new_vals = []
        for i in range(0, 9, 3):
            a, b, c = self.vals[i], self.vals[i + 1], self.vals[i + 2]
            for col in range(3):
                nv = a*mat.vals[col] + b*mat.vals[col + 3] + c*mat.vals[col + 6]
                new_vals.append(nv)
        self.vals = {i:x for i,x in enumerate(new_vals)}
        return
        
        
class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 2:
            return n
        if n == 2:
            return 1
        two = 1
        one = 1
        zero = 0
        cur_mat = Matrix([1, 0, 0, 0, 1, 0, 0, 0, 1])
        pow_2_mat = Matrix([1, 1, 1, 1, 0, 0, 0, 1, 0])
        
        n = n - 2
        while n > 0:
            if n % 2 == 1:
                cur_mat @ pow_2_mat
            pow_2_mat @ pow_2_mat
            n = n >> 1
        last_3 = cur_mat.vec_mult(two, one, zero)
        return last_3[0]
        
        
            