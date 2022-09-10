class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = set(['+', '-', '*', '/'])
        
        for tok in tokens:
            if tok in ops:
                r = stack.pop()
                l = stack.pop()
                if tok == '+':
                    stack.append(l + r)
                    
                elif tok == '-':
                    stack.append(l - r)
                    
                elif tok == '*':
                    stack.append(l*r)
                    
                elif tok == "/":
                    if (l >= 0 and r>=0) or (l <= 0 and r <= 0):
                        stack.append(l // r)
                        
                    else:
                        if l%r == 0:
                            stack.append(l // r)
                        else:
                            stack.append(1 + (l // r))
            else:
                stack.append(int(tok))
                
        return stack[-1]