class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.done = False
        
        def isValid(val, r, c):
            for i in range(9):
                if board[r][i] == val or board[i][c] == val:
                    return False
            
            startCol = 3 * (c // 3)
            startRow = 3 * (r // 3)
            for i in range(3):
                for j in range(3):
                    if board[i + startRow][j + startCol] == val:
                        return False
            return True
        
        def nextSpot(r, c):
            if c == 8:
                return r + 1, 0
            return r, c + 1
                
            
        def dfs(r, c):
            newR, newC = nextSpot(r, c)
            if board[r][c] != '.' or self.done:
                if r == 8 and c == 8:
                    self.done = True
                if not self.done:
                    dfs(newR, newC)
            else:
                for v in range(1, 10):
                    strV = str(v)
                    if not self.done and isValid(strV, r, c):
                        board[r][c] = strV
                        if r == 8 and c==8:
                            self.done = True
                        else:
                            dfs(newR, newC)
                if not self.done:
                    board[r][c] = '.'
        dfs(0, 0)
        return board
            
            