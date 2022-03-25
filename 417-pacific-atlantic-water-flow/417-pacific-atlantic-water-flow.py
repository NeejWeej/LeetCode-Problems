class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        stack = []
        m = len(heights)
        n = len(heights[0])
        if n == 1 or m == 1:
            return [[x,y] for x in range(m) for y in range(n)]
        counts = {}
        delta_n = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def valid_neighs(x,y):
            neighs = []
            for dx, dy in delta_n:
                if 0 <= dx + x < m and 0 <= dy + y < n:
                    neighs.append((dx + x, dy + y))
            return neighs
        
        def dfs(shift, error_region):
            while stack:
                x, y, val = stack.pop()[:]
                neighs = valid_neighs(x,y)
                for nx, ny in neighs:
                    nval = heights[nx][ny]
                    if counts.get((nx, ny), 0) not in error_region:
                        if nval >= val:
                            stack.append((nx, ny, nval))
                            counts[(nx,ny)] = counts.get((nx, ny), 0) + shift
                            
        def set_row_col(row, v, shift):
            if row:
                for i in range(n):
                    if i == 0 and v == 0:
                        continue
                    if i == n - 1 and v == m - 1:
                        continue
                    stack.append((v,i,heights[v][i]))
                    counts[(v,i)] = counts.get((v,i), 0) + shift
                    
            else:
                for i in range(m):
                    stack.append((i,v, heights[i][v]))
                    counts[(i,v)] = counts.get((i,v), 0) + shift
                    
        set_row_col(True, 0, 1)
        set_row_col(False, 0, 1)
        dfs(1, set([1]))

        set_row_col(True, m - 1, 3)
        set_row_col(False, n - 1, 3)
        dfs(3, set([3, 4]))

        ans = [[x,y] for (x,y), val in counts.items() if val == 4]
        return ans
        
        
            
            
            
            
        
        
        