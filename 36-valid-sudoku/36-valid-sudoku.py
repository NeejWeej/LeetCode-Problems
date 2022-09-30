class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def updateSeen(seen, char):
            if char != '.':
                if char in seen:
                    return False
                seen.add(char)
            return True
                
        def checkCol(c):
            seen = set()
            for i in range(9):
                char = board[i][c]
                if not updateSeen(seen, char):
                    return False
            return True
        
        def checkRow(r):
            seen = set()
            for i in range(9):
                char = board[r][i]
                if not updateSeen(seen, char):
                    return False
            return True
        
        def checkBox(num):
            startR = 3*(num//3)
            startC = 3*(num%3)
            seen = set()
            for r in range(startR, startR + 3):
                for c in range(startC, startC + 3):
                    char = board[r][c]
                    if not updateSeen(seen, char):
                        return False
            return True
        
        for i in range(9):
            if not checkBox(i) or not checkRow(i) \
            or not checkCol(i):
                return False
        return True
                
            
            
        