class Solution:
    def __init__(self):
        self. neighbors = [(0,1), (1,0), (0, -1), (-1, 0)]
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #left pacific
        #right atlantic
        rows = len(heights)
        cols = len(heights[0])
        result = [[[0,0] for j in range(len(heights[0]))] for i in range(len(heights))]
        visited_p = set()
        visited_a = set()
        p_stack = []
        a_stack = []
        for j in range(max(rows,cols)):
            if j < rows:
                p_stack.append((j,0))
                a_stack.append((j, cols - 1))
                visited_p.add((j,0))
                visited_a.add((j, cols - 1))
            if j < cols:
                visited_p.add((0, j))
                visited_a.add((rows - 1, j))
                p_stack.append((0,j))
                a_stack.append((rows - 1, j))
        while p_stack:
            curr = p_stack.pop()
            result[curr[0]][curr[1]][0] = 1
            new_neighbors = [ (curr[0] + i, curr[1] + j) for i,j in self.neighbors]
            for x,y in new_neighbors:
                if 0<= x and x < rows and 0 <= y and y < cols:
                    if (x,y) not in visited_p and heights[x][y] >= heights[curr[0]][curr[1]]:
                        visited_p.add((x,y))
                        p_stack.append((x,y))
        while a_stack:
            curr = a_stack.pop()
            result[curr[0]][curr[1]][1] = 1
            new_neighbors = [ (curr[0] + i, curr[1] + j) for i,j in self.neighbors]
            for x,y in new_neighbors:
                if 0<= x and x < rows and 0 <= y and y < cols:
                    if (x,y) not in visited_a and heights[x][y] >= heights[curr[0]][curr[1]]:
                        visited_a.add((x,y))
                        a_stack.append((x,y))
        ans = []
        for i in range(rows):
            for j in range(cols):
                if result[i][j][0] == 1 and result[i][j][1] == 1:
                    ans.append([i,j])
        return ans