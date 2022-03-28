class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for _ in range(n)] for _ in range(n)]
        ans = []
        
        def check_diag(x, x_increasing, y, y_increasing):
            dx = 1 if x_increasing == 1 else -1
            dy = 1 if y_increasing == 1 else -1
            while 0 <= x < n and 0 <= y < n:
                if board[x][y] == 'Q':
                    return False
                x += dx
                y += dy
            return True
        
        def check_spot(x, y):
            for r in range(n):
                if board[r][y] == 'Q':
                    return False
                if board[x][r] == 'Q':
                    return False
            for i in range(4):
                x_direc = i % 2
                y_direc = (i >> 1) % 2
                if not check_diag(x, x_direc, y, y_direc):
                    return False
            return True
            
            
        def dfs(row):
            if row == n:
                ans.append(["".join(row) for row in board])
                return
            for i in range(n):
                if check_spot(row, i):
                    board[row][i] = 'Q'
                    dfs(row + 1)
                    board[row][i] = '.'
        dfs(0)
        return ans
            