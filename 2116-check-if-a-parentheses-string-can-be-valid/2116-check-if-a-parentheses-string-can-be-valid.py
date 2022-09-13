class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2:
            return False
        
        stackL = []
        stackU = []
        for i, c in enumerate(s):
            if locked[i] == '1':
                if c == '(':
                    stackL.append(i)
                elif c == ')':
                    if stackL:
                        stackL.pop()
                    elif stackU:
                        stackU.pop()
                    else:
                        return False
            else:
                stackU.append(i)
        
        if len(stackL) > len(stackU):
            return False
        
        while stackL:
            if stackU[-1] < stackL[-1]:
                return False
            stackU.pop()
            stackL.pop()
                
        return not len(stackU) % 2 
                