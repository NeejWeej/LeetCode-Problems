class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        oldColor = image[sr][sc]
        if oldColor == newColor:
            return image
        m = len(image)
        n = len(image[0])
        direc = [(0,1), (1, 0), (-1, 0), (0, -1)]
        stack = [(sr, sc)]
        image[sr][sc] = newColor
        
        while stack:
            x,y = stack.pop()[:]
            for dx, dy in direc:
                if 0 <= x + dx < m and 0 <= y + dy < n:
                    if image[x + dx][y + dy] == oldColor:
                        stack.append((x + dx, y + dy))
                        image[x + dx][y + dy] = newColor
        return image
        