import collections

class Solution:
    def __init__(self):
        self.neighbors = [(0,1), (1,0), (0, -1), (-1, 0)]
    
    def dfs(self, visited, heights, row, col, results, Atlantic):
        def is_valid(heights, r, c):
            return (0 <= r and 0 <= c and r < len(heights) and c < len(heights[0]))
        visited.add((row, col))
        if (row == 0 or col == 0):
            results[row][col][0] = True
            if Atlantic:
                return
        
        if (row == len(heights) - 1) or (col == len(heights[0]) - 1):
            results[row][col][1] = True
            if not Atlantic:
                return
        
        new_neighbs = [(row + i, col + j) for i,j in self.neighbors]
        for r,c in new_neighbs:
            if not is_valid(heights, r, c) or heights[row][col] < heights[r][c]:
                continue
            if (r,c) not in visited:
                self.dfs(visited, heights, r, c, results, Atlantic)
            new_posibs = results[r][c]
            cur_atl, cur_pac = results[row][col][:]
            results[row][col] = [new_posibs[0] or cur_atl, new_posibs[1] or cur_pac]
        return
    
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        results = [[[False, False] for __ in range(cols)] for _ in range(rows)]
        
        for r in range(rows):
            results[r][0][0] = True
            results[r][-1][1] = True
        
        for c in range(cols):
            results[0][c][0] = True
            results[-1][c][1] = True
                
        visited = set()
        for r in range(rows):
            for c in range(cols):
                self.dfs(visited, heights, r, c, results, True)
                
        visited = set()
        for r in range(rows):
            for c in range(cols):
                self.dfs(visited, heights, r, c, results, False)
        ans = []
        for r in range(rows):
            for c in range(cols):
                if results[r][c][0] and results[r][c][1]:
                    ans.append((r,c))
        return ans

            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # rows = len(heights)
        # cols = len(heights[0])
        # result = [[[0,0] for j in range(len(heights[0]))] for i in range(len(heights))]
        # visited_p = set()
        # visited_a = set()
        # p_stack = []
        # a_stack = []
        # for j in range(max(rows,cols)):
        #     if j < rows:
        #         p_stack.append((j,0))
        #         a_stack.append((j, cols - 1))
        #         visited_p.add((j,0))
        #         visited_a.add((j, cols - 1))
        #     if j < cols:
        #         visited_p.add((0, j))
        #         visited_a.add((rows - 1, j))
        #         p_stack.append((0,j))
        #         a_stack.append((rows - 1, j))
        # while p_stack:
        #     curr = p_stack.pop()
        #     result[curr[0]][curr[1]][0] = 1
        #     new_neighbors = [ (curr[0] + i, curr[1] + j) for i,j in self.neighbors]
        #     for x,y in new_neighbors:
        #         if 0<= x and x < rows and 0 <= y and y < cols:
        #             if (x,y) not in visited_p and heights[x][y] >= heights[curr[0]][curr[1]]:
        #                 visited_p.add((x,y))
        #                 p_stack.append((x,y))
        # while a_stack:
        #     curr = a_stack.pop()
        #     result[curr[0]][curr[1]][1] = 1
        #     new_neighbors = [ (curr[0] + i, curr[1] + j) for i,j in self.neighbors]
        #     for x,y in new_neighbors:
        #         if 0<= x and x < rows and 0 <= y and y < cols:
        #             if (x,y) not in visited_a and heights[x][y] >= heights[curr[0]][curr[1]]:
        #                 visited_a.add((x,y))
        #                 a_stack.append((x,y))
        # ans = []
        # for i in range(rows):
        #     for j in range(cols):
        #         if result[i][j][0] == 1 and result[i][j][1] == 1:
        #             ans.append([i,j])
        # return ans