class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        leftSet = set(['[', '(', '{'])
        match = {'}':'{', ')': '(', ']':'['}
        for c in s:
            if c in match:
                if stack and stack[-1] == match.get(c):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack