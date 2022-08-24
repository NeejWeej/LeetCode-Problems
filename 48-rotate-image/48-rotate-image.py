class Solution:
    from collections import deque
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)  
        
        def rotateRecurse(bounds):
            rowStart = colStart = bounds
            # end is not inclusive!
            rowEnd = colEnd = n - bounds
            if rowEnd - rowStart <= 1:
                return
            deq = deque([])
            for c in range(colStart, colEnd - 1):
                deq.append(matrix[rowStart][c])
                    
            for r in range(rowStart, rowEnd - 1):
                deq.append(matrix[r][colEnd - 1])
                matrix[r][colEnd - 1] = deq.popleft()
            
            for c in range(colEnd - 1, colStart, -1):
                deq.append(matrix[rowEnd - 1][c])
                matrix[rowEnd - 1][c] = deq.popleft()
            
            for r in range(rowEnd - 1, rowStart, -1):
                deq.append(matrix[r][colStart])
                matrix[r][colStart] = deq.popleft()
                        
            for c in range(colStart, colEnd - 1):
                matrix[rowStart][c] = deq.popleft()
        
        for i in range((n + 1) // 2):
            rotateRecurse(i)
        return
                    
        