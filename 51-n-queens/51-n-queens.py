class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        start = [["." for _ in range(n)] for _ in range(n)]
        def isValid(n, board, x, y):
            for i in range(n):
                if board[i][y] == "Q":
                    return False
            # only need diagonals on higher rows, not lower
            diags = [(-1, 1), (-1, -1)]
            for dx, dy in diags:
                nx, ny= x,y
                while 0<=nx<n and 0<=ny<n:
                    if board[nx][ny] == 'Q':
                        return False
                    nx += dx
                    ny += dy
            return True
        def recursive(board, row, outputs):
            if row == n:
                outputs.append(["".join(x) for x in board])
                return
            for y in range(n):
                if isValid(n, board, row, y):
                    # print(board, row, y)
                    board[row][y] = "Q"
                    recursive(board, row + 1, outputs)
                    board[row][y] = "."
        ans = []
        recursive(start, 0, ans)
        return ans
            
            
            
            