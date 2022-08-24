class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        # x,y -> y,-x
        def rotateClock(matrix):
            for r in range(n):
                for c in range(r + 1, n):
                    matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
            
            for r in range(n):
                for c in range(n // 2):
                    matrix[r][c], matrix[r][-c-1] = matrix[r][-c-1], matrix[r][c]
            
            return matrix
        
        def checkEqual(m1, m2):
            for i in range(n):
                for j in range(n):
                    if m1[i][j] != m2[i][j]:
                        return False
            return True
        
        for _ in range(4):
            if checkEqual(mat, target):
                return True
            mat = rotateClock(mat)
        
        return False
            