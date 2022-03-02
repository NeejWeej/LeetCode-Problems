class Solution:
    
    def dfs(self, board, next_idx, word, row, col, m, n, seen):
        if next_idx == len(word):
            return True
        
        seen.add((row, col))
        
        for n_r, n_c in ((row, 1 + col), (row, col - 1), (row + 1, col), (row - 1, col)):
            if (0<=n_r<m and 0<=n_c<n) and (n_r, n_c) not in seen \
                and word[next_idx] == board[n_r][n_c] \
                and self.dfs(board, next_idx + 1, word, n_r, n_c, m, n, seen):
                    return True
        seen.remove((row,col))
        return False
                
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0] and self.dfs(board, 1, word, r, c, m, n, set()):
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
        