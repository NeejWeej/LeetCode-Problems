class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visited = set()
        m = len(matrix)
        if m == 1:
            return [x for x in matrix[0]]
        n = len(matrix[0])
        if n == 1:
            return [matrix[i][0] for i in range(m)]
        ans = []
        # right, left, down, up
        r = c = 0
        def oneD(r, c, change, row):
            ans.append(matrix[r][c])
            visited.add((r,c))
            if row:
                r += change
            else:
                c += change
            return r,c

        while True:
            while c < n and (r,c) not in visited:
                r,c = oneD(r,c, 1, False)
            c -= 1
            r += 1
            if r == m or (r, c) in visited: return ans
            while r < m and (r, c) not in visited:
                r,c = oneD(r,c, 1, True)
            r -= 1
            c -= 1
            if c < 0 or (r, c) in visited: return ans
            while c >= 0 and (r,c) not in visited:
                r,c = oneD(r,c, -1, False)
            c += 1
            r -= 1
            if r < 0 or (r, c) in visited: return ans
            while r >= 0 and (r,c) not in visited:
                r,c = oneD(r,c, -1, True)
            r += 1
            c += 1
            if c == n or (r, c) in visited: return ans
            
            