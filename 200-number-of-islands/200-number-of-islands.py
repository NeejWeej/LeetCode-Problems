class Solution:
    
    def dfs(self, grid, r, c, visited, rows, cols):
        visited.add((r,c))
        for x,y in ((1,0), (-1, 0), (0, 1), (0, -1)):
            new_n = (x + r, y + c)
            if 0 <= new_n[0] < rows and 0<= new_n[1] < cols and new_n not in visited:
                if grid[new_n[0]][new_n[1]] == '1':
                    self.dfs(grid, new_n[0], new_n[1], visited, rows, cols)
        return
        
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        ans = 0
        rows = len(grid)
        cols = len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visited:
                    ans += 1
                    self.dfs(grid, r, c, visited, rows, cols)
        return ans
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # self.neighbs = [(0,1), (0,-1), (1,0), (-1,0)]
        # visited = set()
        # count = 0
        # stack = []
        # def neighbors(x,y):
        #     poss = [(x + i, y + j) for i,j in self.neighbs]
        #     ans = []
        #     for v,w in poss:
        #         if (v,w) in visited:
        #             continue
        #         if 0 <= v and v < len(grid) and 0<= w and w < len(grid[0]):
        #             ans.append((v,w))
        #     return ans
        # for r in range(len(grid)):
        #     for c in range(len(grid[0])):
        #         if (r,c) in visited or grid[r][c] == '0':
        #             continue
        #         stack = [(r,c)]
        #         while stack:
        #             cur = stack.pop()
        #             neighs = neighbors(cur[0], cur[1])
        #             for n in neighs:
        #                 if grid[n[0]][n[1]] == '1':
        #                     visited.add(n)
        #                     stack.append(n)
        #         count += 1
        # return count