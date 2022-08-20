class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])
        self.pm = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        
#         vertCur = horzCur = matrix[0][0]
#         self.pm[0][0] = horzCur
#         for i in range(1, n):
#             horzCur += matrix[0][i]
#             self.pm[0][i] = horzCur
            
#         vertCur = matrix[0][0]
#         for i in range(1, m):
#             vertCur += matrix[i][0]
#             self.pm[i][0] = vertCur
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.pm[i][j] = \
                    matrix[i - 1][j - 1] + self.pm[i-1][j] + self.pm[i][j-1] - self.pm[i-1][j-1]
                

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        return self.pm[row2 + 1][col2 + 1] - self.pm[row1][col2 + 1] - self.pm[row2 + 1][col1] + \
        self.pm[row1][col1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)