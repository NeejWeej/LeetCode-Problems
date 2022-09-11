class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        origColor = image[sr][sc]
        
        if origColor == color:
            return image
        
        image[sr][sc] = color
        
        direc = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def isValid(r, c):
            return 0<=r<m and 0<=c<n
        
        
        q = [(sr, sc)]
        while q:
            nextQ = []
            for r,c in q:
                for dx, dy in direc:
                    if isValid(r+dx, c+dy) and image[r+dx][c+dy] == origColor:
                        image[r+dx][c+dy] = color
                        nextQ.append((r+dx, c+dy))
            q = nextQ
        
        return image