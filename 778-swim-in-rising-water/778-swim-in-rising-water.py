class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        left = max(n - 1, grid[0][0])
        right = n*n
        
        def canDo(val):
            visited = set()
            stack = [(0,0)]
            direc = [(0, 1), (-1, 0), (0, -1), (1, 0)]
            while stack:
                x,y = stack.pop()
                if x == n-1 and y == n-1:
                    return True
                visited.add((x,y))
                for dx, dy in direc:
                    if 0 <= x+dx < n and 0<=y+dy<n:
                        if (x+dx, y+dy) not in visited and grid[x+dx][y+dy] <= val:
                            stack.append((x + dx, y + dy))
            return False     
            
        while left < right:
            mid = (left + right) // 2
            if canDo(mid):
                right = mid
            else:
                left = mid + 1
                
        return left
        
        