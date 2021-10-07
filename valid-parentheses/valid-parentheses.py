class Solution:
    import collections
    def isValid(self, s: str) -> bool:
        order = collections.deque([])
        stack = []
        closing_pair = {'(' : ')', '[': ']', '{': '}'}
        
        Open = ['(', '[', '{']
        Close = [')', ']', '}']
        
        for char in s:
            if char in Open:
                stack.append(closing_pair.get(char))
            elif char in Close:
                if len(stack) == 0:
                    return False
                should_be = stack.pop()
                if char != should_be:
                    return False
        
        return len(stack) == 0
        