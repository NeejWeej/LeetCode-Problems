class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m = len(matrix)
        n = len(matrix[0])
        top = left = 0
        bot = m - 1
        right = n - 1
        
        res = []
        def matrixDone(top, bot, left, right):
            return  top > bot or left > right
        
        while True:
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1
            if matrixDone(top, bot, left, right):
                return res
                
            for i in range(top, bot + 1):
                res.append(matrix[i][right])  
            right -= 1
            if matrixDone(top, bot, left, right):
                return res
                
            for i in range(right, left - 1, -1):
                res.append(matrix[bot][i])   
            bot -= 1
            if matrixDone(top, bot, left, right):
                return res
            
            for i in range(bot, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
            
            if matrixDone(top, bot, left, right):
                return res
            
            
        
                
        