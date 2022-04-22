class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        new_rotting = []
        rows = len(grid)
        cols = len(grid[0])
        neighs = [(0,1), (1, 0), (-1, 0), (0, -1)]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    new_rotting.append((r,c))
        minutes = 0
        while new_rotting:
            next_rotting = []
            for r, c in new_rotting:
                for dx, dy in neighs:
                    if 0<=r+dx<rows and 0<=c+dy<cols and grid[r + dx][c + dy] == 1:
                        grid[r + dx][c + dy] = 2
                        next_rotting.append((r + dx,c + dy))
            # print(new_rotting, next_rotting)
            if not next_rotting:
                break
            minutes += 1
            new_rotting = next_rotting
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        return minutes