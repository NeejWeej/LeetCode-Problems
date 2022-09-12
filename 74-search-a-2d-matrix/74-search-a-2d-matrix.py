class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        if matrix[-1][-1] < target:
            return False
        
        l, r = 0, m*n
        
        while l < r:
            mid = (l + r) // 2
            # gives spot in matrix, now get coords
            mr, mc = mid // n, mid % n
            
            val = matrix[mr][mc]
            
            if val == target:
                return True 
            
            elif val < target:
                l = mid + 1
            
            elif val > target:
                r = mid - 1
                
        return matrix[l // n][l % n] == target