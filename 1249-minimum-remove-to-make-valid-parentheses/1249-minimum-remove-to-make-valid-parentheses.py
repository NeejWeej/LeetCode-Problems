class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        count = 0
        
        for c in s:
            if c == '(':
                count += 1
                stack.append(c)
                continue
            if c == ')' and count <= 0:
                continue
            if c == ')':
                count -= 1
                stack.append(c)
                continue
            stack.append(c)
        reverse_stack = stack[::-1]
        stack = []
        count = 0
        for c in reverse_stack:
            if c == ')':
                count += 1
                stack.append(c)
                continue
            if c == '(' and count <= 0:
                continue
            if c == '(':
                count -= 1
                stack.append(c)
                continue
            stack.append(c)     
        return "".join(stack[::-1])
            