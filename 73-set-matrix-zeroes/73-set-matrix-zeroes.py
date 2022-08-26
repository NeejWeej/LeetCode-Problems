class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        
        def setZero(row, col):
            for i in range(m):
                if matrix[i][col] != 'e':
                    matrix[i][col] = 0
                    
            for j in range(n):
                if matrix[row][j] != 'e':
                    matrix[row][j] = 0
                
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][j] = 'e'
        
                
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 'e':
                    setZero(i, j)
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 'e':
                    matrix[i][j] = 0
                    
        