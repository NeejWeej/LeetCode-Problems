class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        # if m == 1:
        #     return [x for x in matrix[0]]
        n = len(matrix[0])
        if n == 1:
            return [matrix[i][0] for i in range(m)]
        ans = [matrix[0][0]]
        visited = set([(0,0)])
        # right, left, down, up
        r = c = 0
        direc = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while True:
            for dx,dy in direc:
                # print(r,c, visited)
                tripped = False
                r += dx
                c += dy
                while 0<=r<m and 0<=c<n and (r,c) not in visited:
                    visited.add((r,c))
                    ans.append(matrix[r][c])
                    tripped = True
                    r += dx
                    c += dy
                if not tripped: return ans
                r -= dx
                c -= dy
            
            