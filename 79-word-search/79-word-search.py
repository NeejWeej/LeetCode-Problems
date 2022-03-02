class Solution:
    
    def valid(self, m, n, r, c):
        return 0 <= r and r < m and 0 <= c and c < n
    
    def dfs(self, board, next_idx, word, row, col, m, n):
        if next_idx == len(word):
            return True
        
        board[row][col] = '*'
        
        for n_r, n_c in ((row, 1 + col), (row, col - 1), (row + 1, col), (row - 1, col)):
            if self.valid(m,n, n_r, n_c) and word[next_idx] == board[n_r][n_c] \
                and self.dfs(board, next_idx + 1, word, n_r, n_c, m, n):
                    return True
        board[row][col] = word[next_idx - 1]
        return False
                
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        
        seen = {}
        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0] and self.dfs(board, 1, word, r, c, m, n):
                        return True
        return False
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         def search(x, y, cur_word):
#             cur_letter = board[x][y]
#             if cur_letter == '*':
#                 return False
            
#             cur_word += cur_letter
            
#             if cur_word != word[:len(cur_word)]:
#                 return False
            
#             if cur_word == word:
#                 return True
            
#             if len(cur_word) >= len(word):
#                 return False
            
#             board[x][y] = '*'
#             neigh = [(x + k[0], y + k[1]) for k in directions]
            
#             for nb in neigh:
#                 if 0 <= nb[0] and nb[0] < m and 0 <= nb[1] and nb[1] < n:
#                     next_l = board[nb[0]][nb[1]]
#                     if len(cur_word) <= len(word):
#                         if search(nb[0], nb[1], cur_word):
#                             board[x][y] = cur_letter
#                             return True
                        
#             board[x][y] = cur_letter
#             return False
        
#         directions = [(0,1), (0,-1), (1,0), (-1,0)]
        
#         m = len(board)
#         n = len(board[0])
        
#         for i in range(m):
#             for j in range(n):
#                 if search(i,j,''):
#                     return True
        
#         return False
        