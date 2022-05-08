class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        new_rotting = []
        rows = len(grid)
        cols = len(grid[0])
        neighs = [(0,1), (1, 0), (-1, 0), (0, -1)]
        fresh = set([])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    new_rotting.append((r,c))
                elif grid[r][c] == 1:
                    fresh.add((r,c))
        minutes = 0
        while new_rotting and fresh:
            next_rotting = []
            for r, c in new_rotting:
                for dx, dy in neighs:
                    if 0<=r+dx<rows and 0<=c+dy<cols and grid[r + dx][c + dy] == 1:
                        fresh.discard((r + dx, c + dy))
                        grid[r + dx][c + dy] = 2
                        next_rotting.append((r + dx,c + dy))
            minutes += 1
            new_rotting = next_rotting
        if len(fresh) > 0:
            return -1
        return minutes