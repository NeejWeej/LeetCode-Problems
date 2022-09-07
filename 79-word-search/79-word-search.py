class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        wordLen = len(word)
        
        direc = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        self.ans = False
        
        def search(r, c, needIdx):
            old = board[r][c]
            board[r][c] = '$'
            
            if needIdx == wordLen or self.ans:
                self.ans = True
                return
            for dx, dy in direc:
                if 0 <= r+dx<m and 0<=c+dy<n and board[r+dx][c+dy] == word[needIdx]:
                    search(r+dx, c+dy, needIdx + 1)
            board[r][c] = old
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    search(i, j, 1)
                    if self.ans:
                        return True
        return self.ans