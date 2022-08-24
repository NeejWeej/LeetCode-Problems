class Solution:
    from collections import deque
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # x,y -> -y, x -> -x,-y -> y,-x -> x,y
        # above is when going counterclockwise
        # we want to swap horizontally (across columns)
        # then we flip across the off-diagonal (to switch y,x)
        
        n = len(matrix)  
                
        for r in range(n):
            for c in range(n // 2):
                matrix[r][c], matrix[r][-c-1] = matrix[r][-c-1], matrix[r][c]
        
        # swap across off-diagonal
        for r in range(n):
            for c in range(n - r):
                matrix[r][c], matrix[n - 1 - c][n - 1 - r] = matrix[n - 1 - c][n - 1 -r], matrix[r][c]
        return
                
                    
        