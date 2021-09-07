class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.neighbs = [(0,1), (0,-1), (1,0), (-1,0)]
        def neighbors(x,y):
            poss = [(x + i, y + j) for i,j in self.neighbs]
            ans = []
            for v,w in poss:
                if 0 <= v and v < len(grid) and 0<= w and w < len(grid[0]):
                    ans.append((v,w))
            return ans
        visited = set()
        count = 0
        stack = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r,c) in visited or grid[r][c] == '0':
                    continue
                stack = [(r,c)]
                while stack:
                    cur = stack.pop()
                    neighs = neighbors(cur[0], cur[1])
                    for n in neighs:
                        if n not in visited and grid[n[0]][n[1]] == '1':
                            visited.add(n)
                            stack.append(n)
                count += 1
        return count