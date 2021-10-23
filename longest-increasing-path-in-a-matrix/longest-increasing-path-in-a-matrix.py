class Solution:   
    def explore(self, matrix, dp, visited, x, y, to_move):
        val = matrix[x][y]
        rows = len(matrix)
        cols = len(matrix[0])
        neigh = [(i + x, j + y) for i,j in to_move]
        neigh = [n for n in neigh if 0<= n[0] and n[0] < rows and 0<=n[1] and n[1] < cols]
        visited.add((x,y))
        best = 1
        for idx, n in enumerate(neigh):
            if matrix[n[0]][n[1]] <= val:
                continue
            if n in visited:
                best = max(best, 1 + dp[n[0]][n[1]])
            else:
                self.explore(matrix, dp, visited, n[0], n[1], to_move)
                best = max(best, 1 + dp[n[0]][n[1]])
        dp[x][y] = best
        self.best = max(self.best, best)    
        
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        to_move = [(1,0), (0,1), (-1, 0), (0, -1)]
        visited = set()
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[1 for _ in range(cols)] for _ in range(rows)]
        self.best = 1
            
        for i in range(rows):
            for j in range(cols):
                if (i,j) in visited:
                    continue
                self.explore(matrix, dp, visited, i, j, to_move)
        return self.best

        # def explore(self, matrix, dp, visited, x, y):
        #     val = matrix[x][y]
        #     nonlocal to_move
        #     nonlocal rows
        #     nonlocal cols
        #     neigh = [(i + x, j + y) for x,y in to_move]
        #     neigh = [n for n in neigh if 0<= n[0] and n[0] < rows and 0<=n[1] and n[1] < cols]
        #     visited.add((x,y))
        #     best = 1
        #     for idx, n in enumerate(neigh):
        #         if matrix[n[0]][n[1]] < val:
        #             continue
        #         if n in visited:
        #             best = max(best, 1 + dp[n[0]][n[1]])
        #         else:
        #             self.explore(matrix, dp, visited, n[0], n[1])
        #             best = max(best, 1 + dp[n[0]][n[1]])
        #     dp[x][y] = best
        #     self.best = max(self.best)
                    