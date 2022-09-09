class Solution:
    def checkValidString(self, s: str) -> bool:
        lb = ub = 0
        
        for char in s:
            if char == '(':
                ub += 1
                lb += 1
                
            elif char == ')':
                ub -= 1
                lb = max(0, lb - 1)
                if ub < 0:
                    return False
            
            elif char == '*':
                lb = max(0, lb - 1)
                ub += 1
        
        return lb <= 0 <= ub