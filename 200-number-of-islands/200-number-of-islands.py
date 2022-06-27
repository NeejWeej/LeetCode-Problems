class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def search(grid, x, y):
            direc = [(0, 1), (0, -1), (-1, 0), (1, 0)]
            for dx, dy in direc:
                if 0<=x + dx < len(grid) and 0<=y+dy<len(grid[0]):
                    if grid[x+dx][y+dy] == "1":
                        grid[x+dx][y+dy] = -1
                        search(grid, x+dx, y + dy)
        ans = 0
        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if grid[m][n] == "1":
                    grid[m][n] = -1
                    ans += 1
                    search(grid, m, n)
        return ans
        