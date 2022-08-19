class Solution:
    from collections import deque
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        curRow = deque(matrix[0])
        m = len(matrix)
        n = len(matrix[0])
        for i in range(1, m):
            curRow.appendleft(matrix[i][0])
            curRow.pop()
            for idx,val in enumerate(curRow):
                if matrix[i][idx] != val:
                    return False
        
        return True
                