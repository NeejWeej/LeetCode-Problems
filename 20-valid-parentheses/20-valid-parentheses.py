class Solution:
    def isValid(self, s: str) -> bool:
        c2o = {'}': '{', ']': '[', ')': '('}
        stack = []
        for c in s:
            if c not in c2o:
                stack.append(c)
            elif stack and stack[-1] == c2o.get(c):
                    stack.pop()
            else:
                return False
        return len(stack) == 0