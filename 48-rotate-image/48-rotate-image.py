class Solution:
    from collections import deque
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # transpose, then flip the new y-coordinate (swap within columns)
        
        n = len(matrix)  
                
        for c in range(n):
            for r in range(n // 2):
                matrix[r][c], matrix[-r -1][c] = matrix[-r - 1][c], matrix[r][c]
        
        for r in range(n):
            for c in range(r + 1, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        return
                
                    
        