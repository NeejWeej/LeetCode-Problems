class Solution:
    def checkValidString(self, s: str) -> bool:
        uB = lB = 0
        
        for char in s:
            if char == '(':
                uB += 1
                lB += 1       
                
            elif char == ')':
                uB -= 1
                lB = max(0, lB - 1)
                if uB < 0:
                    return False
                
            elif char == '*':
                uB += 1
                lB = max(0, lB - 1)
                
        return lB <= 0 <= uB