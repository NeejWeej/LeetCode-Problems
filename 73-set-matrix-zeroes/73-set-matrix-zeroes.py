class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        cols_seen = set()
        rows_seen = set()
        rows = len(matrix)
        cols = len(matrix[0])
        
        def change_zeroes_col(col):
            for r in range(rows):
                matrix[r][col] = 0
        
        def change_zeroes_row(row):
            for c in range(cols):
                matrix[row][c] = 0
            
        for r in range(rows):
            row_seen = False
            for c in range(cols):
                if c in cols_seen and row_seen:
                    continue
                if matrix[r][c] == 0:
                    cols_seen.add(c)
                    row_seen = True
            if row_seen:
                rows_seen.add(r)
        
        for r in rows_seen:
            change_zeroes_row(r)
        for c in cols_seen:
            change_zeroes_col(c)
        return