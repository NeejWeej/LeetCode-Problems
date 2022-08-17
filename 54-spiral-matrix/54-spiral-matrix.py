class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        row = 0
        col = 0
        m = len(matrix)
        n = len(matrix[0])
        topRowSeen = -1
        botRowSeen = m
        leftColSeen = -1
        rightColSeen = n
        
        res = [matrix[0][0]]
            
        while botRowSeen != topRowSeen or \
        leftColSeen != rightColSeen:
            for idx, (dx, dy) in enumerate(directions):
                row += dx
                col += dy
                while botRowSeen > row > topRowSeen and \
                leftColSeen < col < rightColSeen:
                    res.append(matrix[row][col])
                    row += dx
                    col += dy
                row -= dx
                col -= dy
                if idx == 0: 
                    topRowSeen = max(row, topRowSeen)
                elif idx == 1:
                    rightColSeen = min(col, rightColSeen)
                elif idx == 2:
                    botRowSeen = min(row, botRowSeen)
                elif idx == 3:
                    leftColSeen = max(col, leftColSeen) 
        
        return res
                
        