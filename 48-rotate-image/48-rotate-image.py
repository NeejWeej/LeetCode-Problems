class Solution:
    from collections import deque
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for row in range(n):
            matRow = matrix[row]
            l,r = 0, n - 1
            while l < r:
                matRow[l], matRow[r] = matRow[r], matRow[l]
                l += 1
                r -= 1
        return
                
                
                    
        