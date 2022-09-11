class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        
        direc = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        visited = set()
        
        def valid(r, c):
            return 0<=r<m and 0<=c<n
        
        
        self.ans = []
        def dfs(r, c, height, visited, oldVisited):
            if (r,c) in visited:
                return
            visited.add((r,c))
            if oldVisited and (r,c) in oldVisited:
                self.ans.append([r,c])
                
            for dx, dy in direc:
                if valid(r+dx, c+dy) and heights[r+dx][c+dy]>=height:
                    if (r+dx,c+dy) not in visited:
                        dfs(r+dx, c+dy, heights[r+dx][c+dy], visited, oldVisited)
        
        pacificV = set()
        for c in range(n):
            h = heights[0][c]
            dfs(0, c, h, pacificV, None)
            
        for r in range(m):
            h = heights[r][0]
            dfs(r, 0, h, pacificV, None)
        
        atl = set()
        for c in range(n):
            h = heights[-1][c]
            dfs(m-1, c, h, atl, pacificV)
            
        for r in range(m):
            h = heights[r][-1]
            dfs(r, n-1, h, atl, pacificV)        
        
        
        return self.ans
        
        
            
            
            
            
            
        